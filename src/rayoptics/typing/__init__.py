from typing import Tuple, Literal, Optional

import numpy as np

Vector3 = np.ndarray
Vector2 = np.ndarray
Matrix3 = np.ndarray
Transform3 = Tuple[Optional[Matrix3], Vector3]

DCenterTypes = Literal['decenter', 'reverse', 'dec and return', 'bend']
InteractMode = Literal['transmit', 'reflect', 'dummy']
ZDir = Literal[1, -1]
