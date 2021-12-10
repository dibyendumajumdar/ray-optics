from typing import Tuple, Literal, Optional

import numpy as np

Vector2 = np.ndarray
Vector3 = np.ndarray
Direction3 = np.ndarray
Matrix3 = np.ndarray
Transform3 = Tuple[Matrix3, Vector3]

DCenterTypes = Literal['decenter', 'reverse', 'dec and return', 'bend']
InteractMode = Literal['transmit', 'reflect', 'dummy']
ZDir = Literal[1, -1]
