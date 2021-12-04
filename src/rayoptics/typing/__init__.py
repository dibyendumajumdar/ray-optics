from typing import Tuple, Protocol, Literal, Optional, List, Any, Iterator

import numpy as np

Vector3 = np.ndarray
Vector2 = np.ndarray
Transform3 = Tuple[Vector3, Vector3]
Matrix3 = np.ndarray

DCenterTypes = Literal['decenter', 'reverse', 'dec and return', 'bend']
InteractMode = Literal['transmit', 'reflect', 'dummy']
ZDir = Literal[1, -1]
#
#
class IDecenterData(Protocol):
    dtype: DCenterTypes  # 'decenter', 'reverse', 'dec and return', 'bend'
    dec: Vector3  # x, y, z vertex decenter
    euler: Vector3  # alpha, beta, gamma euler angles
    rot_pt: Vector3  # x, y, z rotation point offset
    rot_mat: Optional[Matrix3]

    def update(self) -> Optional[Matrix3]:
        ...

    def apply_scale_factor(self, scale_factor: float):
        ...

    def tform_before_surf(self) -> Tuple[Optional[Matrix3], Vector3]:
        ...

    def tform_after_surf(self) -> Tuple[Optional[Matrix3], Vector3]:
        ...


class IPhaseElement(Protocol):
    def phase(self, pt, in_dir, srf_nrml, z_dir, wl, n_in, n_out):
        ...
#
#
# class IInterface(Protocol):
#     interact_mode: str  # 'transmit' | 'reflect' | 'dummy'
#     delta_n: float  # refractive index difference across the interface
#     decenter: Optional[IDecenterData]
#     max_aperture: Optional[float]
#     profile_cv: Optional[float]
#     phase_element: Optional[IPhaseElement]
#
#     def update(self) -> None:
#         ...
#
#     def interface_type(self) -> str:
#         ...
#
#     def sync_to_restore(self, opt_model) -> None:
#         ...
#
#     def set_optical_power(self, pwr, n_before, n_after):
#         ...
#
#     def surface_od(self):
#         ...
#
#     def set_max_aperture(self, max_ap: float) -> None:
#         ...
#
#     def intersect(self, p0: Vector3, d: Vector3, eps: float, z_dir: ZDir):
#         ...
#
#     def normal(self, p: Vector3) -> Vector3:
#         ...
#
#     def phase(self, pt, in_dir, srf_nrml, z_dir, wl, n_in, n_out):
#         ...
#
#
# class IMedium(Protocol):
#     label: str
#     n: float
#
#     def name(self) -> str:
#         ...
#
#     def catalog_name(self) -> str:
#         ...
#
#     def rindex(self, wv_nm: float) -> float:
#         ...
#
#
# class IGap(Protocol):
#     thi: float
#
#     def apply_scale_factor(self, scale_factor: float) -> None:
#         ...
#
#
# class ISequentialModel(Protocol):
#     opt_model: 'IOpticalModel'  # Forward reference so must be in quotes?
#     ifcs: List[IInterface]
#     gaps: List[IGap]
#     gbl_tfrms: List[Transform3]
#     lcl_tfrms: List[Transform3]
#     z_dir: List[ZDir]
#     stop_surface: int
#     cur_surface: int
#     wvlns: List[float]
#     rndx: List[List[float]]
#
#     def get_num_surfaces(self) -> int:
#         ...
#
#     def path(self, wl=None, start=None, stop=None, step=1) -> Iterator[Tuple[IInterface, IGap, Transform3, int, ZDir]]:
#         ...
#
#     def reverse_path(self, wl=None, start=None, stop=None, step=-1) -> Iterator[
#         Tuple[IInterface, IGap, Transform3, int, ZDir]]:
#         ...
#
#     def central_rndx(self, i: int) -> float:
#         ...
#
#     def calc_ref_indices_for_spectrum(self, wvls: List[float]) -> List[List[float]]:
#         ...
#
#
# class IWvlSpec(Protocol):
#     central_wvl: float
#
#
# class IPupilSpec(Protocol):
#     optical_spec: 'IOpticalSpecs'
#     key: Tuple[str, str, str]
#     value: float
#     pupil_rays: List[List[float]]
#     ray_labels: List[str]
#
#
# class IField(Protocol):
#     x: float
#     y: float
#     vux: float
#     vuy: float
#     vlx: float
#     vly: float
#     wt: float
#     aim_pt: Any
#     chief_ray: Any
#     ref_sphere: Any
#
#
# class IFocusRange(Protocol):
#     focus_shift: float
#     defocus_range: float
#
#
# class IFieldSpec(Protocol):
#     optical_spec: 'IOpticalSpecs'
#     key: Tuple[str, str, str]
#     value: float
#     is_relative: bool
#     fields: List[IField]
#
#
# class IOpticalSpecs(Protocol):
#     opt_model: 'IOpticalModel'  # Forward reference so must be in quotes?
#     wvls: IWvlSpec
#     pupil: IPupilSpec
#     fov: IFieldSpec
#     focus: IFocusRange
#     parax_data: Any
#
#
# class IOpticalModel(Protocol):
#     seq_model: ISequentialModel
