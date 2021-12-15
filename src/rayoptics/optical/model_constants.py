#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2018 Michael J. Hayford
""" optical model constants

.. Created on Wed May 23 16:00:55 2018

.. codeauthor: Michael J. Hayford
"""

# sequential ray trace data structures
from typing import Final

#Intfc, kGap, Tfrm, Indx, Zdir = range(5)
Intfc: Final = 0
kGap: Final = 1
Tfrm: Final = 2
Indx: Final = 3
Zdir: Final = 4


# Surf, kGap = range(2)
Surf: Final = 0
#kGap: Final = 1

# paraxial optics data structures
# 4 parts of paraxial model: axial ray, principal ray,
#                            lens data, optical invariant
#ax, pr, lns, inv = range(4)
ax: Final = 0
pr: Final = 1
lns: Final = 2
inv: Final = 3
# paraxial ray data at an interface: height, n*slope, n*angle of incidence
#ht, slp, aoi = range(3)
ht: Final = 0
slp: Final = 1
aoi: Final = 2
# lens data: power, reduced distance, refractive index (n), refract mode
#pwr, tau, indx, rmd = range(4)
pwr: Final = 0
tau: Final = 1
indx: Final = 2
rmd: Final = 3

# ray trace segment data
# p: intersection point with interface
# d: direction cosine exiting the interface
# dst: distance from intersection point to next interface
# nrml: surface normal at intersection point
# phase: optical phase introduced at the interface
#p, d, dst, nrml, phase = range(5)
p: Final = 0
d: Final = 1
dst: Final = 2
nrml: Final = 3
phase: Final = 4

# ray package
# ray: list of ray segment data
# op:  optical path wrt equally inclined chords to the optical axis
# wvl: wavelength (in nm) that the ray was traced in
#ray, op, wvl = range(3)
ray: Final = 0
op: Final = 1
wvl: Final = 2
