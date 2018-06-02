#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2018 Michael J. Hayford
""" miscellaneous functions for working with numpy vectors and floats
Created on Wed May 23 15:27:06 2018

@author: Michael J. Hayford
"""
import numpy as np
from numpy.linalg import norm


def normalize(v):
    """ return normalized version of input vector v """
    length = norm(v)
    if length == 0.0:
        return v
    else:
        return v/length


def distance_sqr_2d(pt0, pt1):
    """ return distance squared between 2d points pt0 and pt1 """
    return (pt0[0] - pt1[0])**2 + (pt0[1] - pt1[1])**2


def euler2opt(e):
    """ convert right-handed euler angles to optical design convention,
        i.e. alpha and beta are left-handed
    """
    return np.array([-e[0], -e[1], e[2]])


def isanumber(a):
    """ returns true if input a can be converted to floating point number """
    try:
        float(a)
        bool_a = True
    except ValueError:
        bool_a = False

    return bool_a
