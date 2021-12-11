#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2020 Michael J. Hayford
"""Base class for Interfaces

.. Created on Sat Jun 13 22:04:27 2020

.. codeauthor: Michael J. Hayford
"""


from enum import Enum, auto
from typing import Tuple

from rayoptics.typing import InteractMode, Vector3, ZDir


class InteractionMode(Enum):
    """ enum for different interact_mode specifications

    Retained to restore old files

    .. deprecated:: 0.4.5
    """
    Transmit = auto()  #: propagate in transmission at this interface
    Reflect = auto()   #: propagate in reflection at this interface


class Interface:
    """Basic part of a sequential model

    The :class:`~sequential.SequentialModel` is a sequence of Interfaces and
    Gaps. The Interface class is a boundary between two adjacent Gaps and
    their associated media. It specifies several methods that must be
    implemented to model the optical behavior of the interface.

    The Interface class addresses the following use cases:

        - support for ray intersection calculation during ray tracing
            - interfaces can be tilted and decentered wrt the adjacent gaps
        - support for getting and setting the optical power of the interface
        - support for various optical properties, i.e. does it reflect or
          transmit
        - supports a basic idea of size, the max_aperture

    Attributes:
        interact_mode: 'transmit' | 'reflect' | 'dummy'
        delta_n: refractive index difference across the interface
        decenter: :class:`~rayoptics.elem.surface.DecenterData` for the interface, if specified
        max_aperture: the maximum aperture radius on the interface
    """
    def __init__(self, interact_mode: InteractMode = 'transmit', delta_n: float = 0.0,
                 max_ap: float = 1.0, decenter=None,
                 phase_element=None, **kwargs):
        self.interact_mode: InteractMode = interact_mode
        self.delta_n: float = delta_n
        self.decenter = decenter
        self.max_aperture: float = max_ap
        if phase_element is not None:
            self.phase_element = phase_element

    def update(self) -> None:
        if self.decenter is not None:
            self.decenter.update()

    def interface_type(self):
        return type(self).__name__

    def sync_to_restore(self, opt_model):
        if not hasattr(self, 'max_aperture'):
            self.max_aperture = 1.0
        if hasattr(self, 'interact_mode'):
            # don't know why I need to test for the InteractionMode
            #  enum like this, or have to compare enum values, but
            #  that's what works...
            if isinstance(self.interact_mode, Enum):
                imode = self.interact_mode.value
                if imode == InteractionMode.Reflect.value:
                    self.interact_mode = 'reflect'
                elif imode == InteractionMode.Transmit.value:
                    self.interact_mode = 'transmit'
        if hasattr(self, 'refract_mode'):  # really old models
            if self.refract_mode == 'REFL':
                self.interact_mode = 'reflect'
            else:
                self.interact_mode = 'transmit'
            delattr(self, 'refract_mode')

    @property
    def profile_cv(self) -> float:
        return 0.0

    def set_optical_power(self, pwr: float, n_before: float, n_after: float) -> None:
        pass

    def surface_od(self) -> None:
        pass

    def set_max_aperture(self, max_ap: float) -> None:
        """ max_ap is the max aperture radius """
        self.max_aperture = max_ap

    def intersect(self, p0: Vector3, d: Vector3, eps: float = 1.0e-12, z_dir: ZDir = 1) -> Tuple[float, Vector3]:
        ''' Intersect an :class:`~.Interface`, starting from an arbitrary point.

        Args:
            p0:  start point of the ray in the interface's coordinate system
            d:  direction cosine of the ray in the interface's coordinate system
            z_dir: +1 if propagation positive direction, -1 if otherwise
            eps: numeric tolerance for convergence of any iterative procedure

        Returns:
            tuple: distance to intersection point *s1*, intersection point *p*

        Raises:
            :exc:`~rayoptics.raytr.traceerror.TraceMissedSurfaceError`
        '''
        pass

    def normal(self, p: Vector3) -> Vector3:
        """Returns the unit normal of the interface at point *p*. """
        pass

    def phase(self, pt, in_dir, srf_nrml, z_dir, wl, n_in, n_out):
        """Returns a diffracted ray direction and phase increment.

        Args:
            pt: point of incidence in :class:`~.Interface` coordinates
            in_dir: direction cosine of incident ray
            srf_nrml: :class:`~.Interface` surface normal at pt
            z_dir: -1 if after an odd # of reflections, +1 otherwise
            wl: wavelength in nm for ray, defaults to ref_wl
            n_in: refractive index preceding the interface
            n_out: refractive index following the interface

        Returns:
            (**out_dir, dW**)

            - out_dir: direction cosine of the out going ray
            - dW: phase added by diffractive interaction
        """
        if hasattr(self, 'phase_element'):
            return self.phase_element.phase(pt, in_dir, srf_nrml, z_dir, wl,
                                            n_in, n_out)

    def apply_scale_factor(self, scale_factor: float) -> None:
        self.max_aperture *= scale_factor
        if self.decenter:
            self.decenter.apply_scale_factor(scale_factor)
