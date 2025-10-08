import transforms3d as t3d
import numpy as np

euler1 = np.array([30,40,50])
euler2 = np.deg2rad(euler1)

print(euler2)

euler3 = t3d.euler.euler2mat(euler2[0], euler2[1], euler2[2])

print(euler3)
