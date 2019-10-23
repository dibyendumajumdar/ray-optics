#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2019 Michael J. Hayford
"""
.. Created on Wed Oct 16 14:20:49 2019

.. codeauthor: Michael J. Hayford
"""

import numpy as np

from rayoptics.gui.util import GUIHandle, bbox_from_poly

from rayoptics.optical.model_constants import ht, slp
from rayoptics.util.rgb2mpl import rgb2mpl


class Diagram():
    """ class for paraxial ray rendering/editing """
    def __init__(self, opt_model, dgm_type, seq_start=1,
                 label='paraxial'):
        self.label = label
        self.opt_model = opt_model

        self.dgm_type = dgm_type
        self.setup_dgm_type(dgm_type)

    def setup_dgm_type(self, dgm_type):
        parax_model = self.opt_model.parax_model
        if dgm_type == 'ht':
            self.type_sel = ht
            self._apply_data = parax_model.apply_ht_dgm_data
        elif dgm_type == 'slp':
            self.type_sel = slp
            self._apply_data = parax_model.apply_slope_dgm_data

    def get_label(self):
        return self.label

    def apply_data(self, node, vertex):
        self._apply_data(node, vertex)
        self.opt_model.parax_model.paraxial_lens_to_seq_model()

    def assign_object_to_node(self, node, factory):
        parax_model = self.opt_model.parax_model
        parax_model.assign_object_to_node(node, factory)
        parax_model.paraxial_lens_to_seq_model()

    def register_commands(self, *args, **inputs):
        fig = inputs.pop('figure')
        self.command_inputs = dict(inputs)

        def do_command_action(event, target, event_key):
            nonlocal fig
            if target is not None:
                shape, handle = target.artist.shape
                try:
                    handle_action_obj = shape.actions[handle]
                    handle_action_obj.actions[event_key](fig, event)
                except KeyError:
                    pass
        fig.do_action = do_command_action

    def render_shape(self):
        """ render the diagram into a shape list """
        parax_model = self.opt_model.parax_model
        shape = []
        for x, y in zip(parax_model.pr, parax_model.ax):
            shape.append([x[self.type_sel], y[self.type_sel]])
        return shape


class DiagramNode():
    def __init__(self, diagram, idx):
        self.diagram = diagram
        self.node = idx
        self.select_pt = None
        self.move_direction = None
        self.handles = {}
        self.actions = self.handle_actions()

    def update_shape(self, view):
        n_color = rgb2mpl([138, 43, 226])  # blueviolet
        shape = self.diagram.shape
        num_nodes = len(shape)
        self.handles['shape'] = shape[self.node], 'vertex', {'linestyle': '',
                                                             'marker': 's',
                                                             'picker': 6,
                                                             'color': n_color,
                                                             'hilite': 'red'}
        if self.node > 1 and self.node < num_nodes-1:
            pt0 = shape[self.node-1]
            pt2 = shape[self.node+1]
            seg = [pt0, pt2]
            self.handles['dist'] = seg, 'polyline', {'picker': 6,
                                                     'color': n_color,
                                                     'hilite': 'red'}
        gui_handles = {}
        for key, graphics_handle in self.handles.items():
            poly_data, poly_type, kwargs = graphics_handle
            poly = np.array(poly_data)
            if poly_type == 'vertex':
                priority = 2.5
                p = view.create_vertex(poly, zorder=priority, **kwargs)
            elif poly_type == 'polyline':
                priority = 2.
                p = view.create_polyline(poly, zorder=priority, **kwargs)
            elif poly_type == 'polygon':
                p = view.create_polygon(poly, self.render_color(),
                                        zorder=2.5, **kwargs)
            else:
                break
            if len(poly.shape) > 1:
                bbox = bbox_from_poly(poly)
            else:
                x = poly[0]
                y = poly[1]
                bbox = np.array([[x, y], [x, y]])
            gui_handles[key] = GUIHandle(p, bbox)
        return gui_handles

    def render_color(self):
        e = self.diagram.opt_model.ele_model.elements[self.node]
        return e.render_color

    def get_label(self):
        return 'node' + str(self.node)

    def handle_actions(self):
        actions = {}
        actions['shape'] = EditNodeAction(self)
        actions['dist'] = EditNodeAction(self)
        return actions


class DiagramEdge():
    def __init__(self, diagram, idx):
        self.diagram = diagram
        self.edge = idx
        self.select_pt = None
        self.move_direction = None
        self.handles = {}
        self.actions = self.handle_actions()

    def update_shape(self, view):
        shape = self.diagram.shape
        edge_poly = shape[self.edge:self.edge+2]
        self.handles['shape'] = edge_poly, 'polyline', {'picker': 6,
                                                        'hilite': 'red'}
        area_poly = [[0, 0]]
        area_poly.extend(edge_poly)
        fill_color = self.render_color()
        self.handles['area'] = area_poly, 'polygon', {'fill_color': fill_color}

        gui_handles = {}
        for key, graphics_handle in self.handles.items():
            poly_data, poly_type, kwargs = graphics_handle
            poly = np.array(poly_data)
            if poly_type == 'polygon':
                p = view.create_polygon(poly, self.render_color(),
                                        zorder=2.5, **kwargs)
            elif poly_type == 'polyline':
                priority = 2.
                p = view.create_polyline(poly, zorder=priority, **kwargs)
            else:
                break
            gui_handles[key] = GUIHandle(p, bbox_from_poly(poly))
        return gui_handles

    def render_color(self):
        if self.edge == 0:
            return (237, 243, 254, 64)  # light blue
        else:
            e = self.diagram.opt_model.ele_model.elements[self.edge-1]
            return e.render_color

    def get_label(self):
        return 'edge' + str(self.edge)

    def handle_actions(self):
        actions = {}
        actions['shape'] = AddElementAction(self)
        return actions


class EditNodeAction():
    """ Action to move a diagram node, using an input pt """
    def __init__(self, dgm_node):
        diagram = dgm_node.diagram
        self.cur_node = None

        def on_select(fig, event):
            self.cur_node = dgm_node.node

        def on_edit(fig, event):
            event_data = np.array([event.xdata, event.ydata])
            diagram.apply_data(self.cur_node, event_data)
            fig.refresh_gui()

        def on_release(fig, event):
            event_data = np.array([event.xdata, event.ydata])
            diagram.apply_data(self.cur_node, event_data)
            fig.refresh_gui()
            self.cur_node = None

        self.actions = {}
        self.actions['drag'] = on_edit
        self.actions['press'] = on_select
        self.actions['release'] = on_release


class AddElementAction():
    def __init__(self, dgm_edge, **kwargs):
        diagram = dgm_edge.diagram
        parax_model = diagram.opt_model.parax_model
        self.cur_node = None

        def on_press_add_point(fig, event):
            # if we don't have factory functions, skip the command
            if 'node_init' in diagram.command_inputs and \
               'factory' in diagram.command_inputs:

                self.cur_node = dgm_edge.edge
                event_data = np.array([event.xdata, event.ydata])
                parax_model.add_node(self.cur_node, event_data,
                                     diagram.type_sel)
                self.cur_node += 1
                node_init = diagram.command_inputs['node_init']
                diagram.assign_object_to_node(self.cur_node, node_init)
                fig.skip_build = False
                fig.refresh_gui()

        def on_drag_add_point(fig, event):
            if self.cur_node is not None:
                event_data = np.array([event.xdata, event.ydata])
                diagram.apply_data(self.cur_node, event_data)
                fig.refresh_gui()

        def on_release_add_point(fig, event):
            if self.cur_node is not None:
                factory = diagram.command_inputs['factory']
                diagram.assign_object_to_node(self.cur_node, factory)
                fig.skip_build = False
                fig.refresh_gui()
            self.cur_node = None

        self.actions = {}
        self.actions['press'] = on_press_add_point
        self.actions['drag'] = on_drag_add_point
        self.actions['release'] = on_release_add_point
