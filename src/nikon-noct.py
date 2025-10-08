from rayoptics.environment import *
from rayoptics.seq.medium import InterpolatedGlass
from rayoptics.elem.layout import LensLayout

# New glass types
# d,F,C,g
g738323 = InterpolatedGlass('J-KZFH9', [
    (1013.98, 1.71491), 
    (852.11, 1.72020), 
    (768.195, 1.724010), 
    (706.519, 1.727619),
    (656.273, 1.731309), 
    (643.847, 1.732358), 
    (632.816, 1.733341), 
    (589.294, 1.737801),
    (587.562, 1.738000), 
    (546.074, 1.743413), 
    (486.133, 1.754185), 
    (479.992, 1.755563), 
    (435.835, 1.767673), 
    (404.656, 1.779490)])

opm = OpticalModel()
sm  = opm.seq_model
osp = opm.optical_spec
pm = opm.parax_model
osp.pupil = PupilSpec(osp, key=['image', 'f/#'], value=0.98)
osp.field_of_view = FieldSpec(osp, key=['object', 'angle'], flds=[0., 19.98])
osp.spectral_region = WvlSpec([(486.1327, 0.5), (587.5618, 1.0), (656.2725, 0.5)], ref_wl=1)
opm.system_spec.title = 'WO2019-229849 Example 1 (Nikkor Z 58mm f/0.95 S)'
opm.system_spec.dimensions = 'MM'
opm.radius_mode = True
sm.gaps[0].thi=1e10
sm.add_surface([108.488,7.65,1.90265,35.77])
sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=108.488, cc=0,
        coefs=[0.0,-3.82177e-07,-6.06486e-11,-3.80172e-15,-1.32266e-18,0,0])
sm.ifcs[sm.cur_surface].max_aperture = 33.4
sm.add_surface([-848.55,2.8,1.55298,55.07])
sm.ifcs[sm.cur_surface].max_aperture = 32.91
sm.add_surface([50.252,18.12])
sm.ifcs[sm.cur_surface].max_aperture = 28.97
sm.add_surface([-60.72,2.8,1.61266,44.46])
sm.ifcs[sm.cur_surface].max_aperture = 29.14
sm.add_surface([2497.5,9.15,1.59319,67.9])
sm.ifcs[sm.cur_surface].max_aperture = 32.66
sm.add_surface([-77.239,0.4])
sm.ifcs[sm.cur_surface].max_aperture = 32.66
sm.add_surface([113.763,10.95,1.8485,43.79])
sm.ifcs[sm.cur_surface].max_aperture = 35.45
sm.add_surface([-178.06,0.4])
sm.ifcs[sm.cur_surface].max_aperture = 35.45
sm.add_surface([70.659,9.74,1.59319,67.9])
sm.ifcs[sm.cur_surface].max_aperture = 32.5
sm.add_surface([-1968.5,0.2])
sm.ifcs[sm.cur_surface].max_aperture = 32.5
sm.add_surface([289.687,8,1.59319,67.9])
sm.ifcs[sm.cur_surface].max_aperture = 30.53
sm.add_surface([-97.087,2.8,1.738,32.33])
sm.ifcs[sm.cur_surface].max_aperture = 29.71
sm.add_surface([47.074,8.7])
sm.ifcs[sm.cur_surface].max_aperture = 25.12
sm.add_surface([0,5.29])
sm.set_stop()
sm.ifcs[sm.cur_surface].max_aperture = 23.959
sm.add_surface([-95.23,2.2,1.61266,44.46])
sm.ifcs[sm.cur_surface].max_aperture = 24.96
sm.add_surface([41.204,11.55,1.49782,82.57])
sm.ifcs[sm.cur_surface].max_aperture = 24.96
sm.add_surface([-273.092,0.2])
sm.ifcs[sm.cur_surface].max_aperture = 24.96
sm.add_surface([76.173,9.5,1.883,40.69])
sm.ifcs[sm.cur_surface].max_aperture = 25.56
sm.add_surface([-101.575,0.2])
sm.ifcs[sm.cur_surface].max_aperture = 25.56
sm.add_surface([176.128,7.45,1.95375,32.33])
sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=176.128, cc=0,
        coefs=[0.0,-1.15028e-06,-4.51771e-10,2.7267e-13,-7.66812e-17,0,0])
sm.ifcs[sm.cur_surface].max_aperture = 23.4
sm.add_surface([-67.221,1.8,1.738,32.33])
sm.ifcs[sm.cur_surface].max_aperture = 22.68
sm.add_surface([55.51,2.68])
sm.ifcs[sm.cur_surface].max_aperture = 19.92
sm.add_surface([71.413,6.35,1.883,40.69])
sm.ifcs[sm.cur_surface].max_aperture = 19.73
sm.add_surface([-115.025,1.81,1.69895,30.13])
sm.ifcs[sm.cur_surface].max_aperture = 19.73
sm.add_surface([46.943,0.8])
sm.ifcs[sm.cur_surface].max_aperture = 19.73
sm.add_surface([55.281,9.11,1.883,40.69])
sm.ifcs[sm.cur_surface].max_aperture = 19.47
sm.add_surface([-144.041,3,1.76554,46.76])
sm.ifcs[sm.cur_surface].max_aperture = 19.14
sm.add_surface([52.858,14.5])
sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=52.858, cc=0,
        coefs=[0.0,3.18645e-06,-1.14718e-08,7.74567e-11,-2.24225e-13,3.3479e-16,-1.7047e-19])
sm.ifcs[sm.cur_surface].max_aperture = 19.14
sm.add_surface([0,1.6,1.5168,64.14])
sm.ifcs[sm.cur_surface].max_aperture = 22.15
sm.add_surface([0,1])
sm.ifcs[sm.cur_surface].max_aperture = 22.15

# sm.gaps[0].thi=1e10
# sm.add_surface([108.488,7.65,'J-LASFH9A', 'Hikari'])  # 1.90265,35.77
# sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=108.488, cc=0,
#         coefs=[0.0,-3.82177e-07,-6.06486e-11,-3.80172e-15,-1.32266e-18,0,0])
# sm.ifcs[sm.cur_surface].max_aperture = 33.4
# sm.add_surface([-848.55,2.8,'J-KZFH4', 'Hikari'])   # 1.55298,55.07
# sm.ifcs[sm.cur_surface].max_aperture = 32.91
# sm.add_surface([50.252,18.12])
# sm.ifcs[sm.cur_surface].max_aperture = 28.97
# sm.add_surface([-60.72,2.8,'J-KZFH1', 'Hikari'])    # 1.61266,44.46
# sm.ifcs[sm.cur_surface].max_aperture = 29.14
# sm.add_surface([2497.5,9.15,'J-PSKH1', 'Hikari'])   # 1.59319,67.9
# sm.ifcs[sm.cur_surface].max_aperture = 32.66
# sm.add_surface([-77.239,0.4])
# sm.ifcs[sm.cur_surface].max_aperture = 32.66
# sm.add_surface([113.763,10.95,'J-LASFH22', 'Hikari']) # 1.8485,43.79
# sm.ifcs[sm.cur_surface].max_aperture = 35.45
# sm.add_surface([-178.06,0.4])
# sm.ifcs[sm.cur_surface].max_aperture = 35.45
# sm.add_surface([70.659,9.74,'J-PSKH1', 'Hikari'])   # 1.59319,67.9
# sm.ifcs[sm.cur_surface].max_aperture = 32.5
# sm.add_surface([-1968.5,0.2])
# sm.ifcs[sm.cur_surface].max_aperture = 32.5
# sm.add_surface([289.687,8,'J-PSKH1', 'Hikari'])     # 1.59319,67.9
# sm.ifcs[sm.cur_surface].max_aperture = 30.53
# sm.add_surface([-97.087,2.8,'S-NBH53V', 'Ohara'])   # 1.738,32.33])
# sm.gaps[sm.cur_surface].medium = g738323            # New type J-KZFH9
# sm.ifcs[sm.cur_surface].max_aperture = 29.71
# sm.add_surface([47.074,8.7])
# sm.ifcs[sm.cur_surface].max_aperture = 25.12
# sm.add_surface([0,5.29])
# sm.set_stop()
# sm.ifcs[sm.cur_surface].max_aperture = 23.959
# sm.add_surface([-95.23,2.2,'J-KZFH1', 'Hikari'])    # 1.61266,44.46
# sm.ifcs[sm.cur_surface].max_aperture = 24.96
# sm.add_surface([41.204,11.55,'J-FKH1','Hikari'])     # 1.49782,82.57
# sm.ifcs[sm.cur_surface].max_aperture = 24.96
# sm.add_surface([-273.092,0.2])
# sm.ifcs[sm.cur_surface].max_aperture = 24.96
# sm.add_surface([76.173,9.5,'J-LASF08A', 'Hikari'])   # 1.883,40.69
# sm.ifcs[sm.cur_surface].max_aperture = 25.56
# sm.add_surface([-101.575,0.2])
# sm.ifcs[sm.cur_surface].max_aperture = 25.56
# sm.add_surface([176.128,7.45,'J-LASFH21','Hikari'])  # 1.95375,32.33
# sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=176.128, cc=0,
#         coefs=[0.0,-1.15028e-06,-4.51771e-10,2.7267e-13,-7.66812e-17,0,0])
# sm.ifcs[sm.cur_surface].max_aperture = 23.4
# sm.add_surface([-67.221,1.8,'S-NBH53V', 'Ohara'])   # 1.738,32.33])
# sm.gaps[sm.cur_surface].medium = g738323             # New type J-KZFH9
# sm.ifcs[sm.cur_surface].max_aperture = 22.68
# sm.add_surface([55.51,2.68])
# sm.ifcs[sm.cur_surface].max_aperture = 19.92
# sm.add_surface([71.413,6.35,'J-LASF08A', 'Hikari'])    # 1.883,40.69
# sm.ifcs[sm.cur_surface].max_aperture = 19.73
# sm.add_surface([-115.025,1.81,'J-SF15', 'Hikari'])     # 1.69895,30.13
# sm.ifcs[sm.cur_surface].max_aperture = 19.73
# sm.add_surface([46.943,0.8])
# sm.ifcs[sm.cur_surface].max_aperture = 19.73
# sm.add_surface([55.281,9.11,'J-LASF08A', 'Hikari'])    # 1.883,40.69
# sm.ifcs[sm.cur_surface].max_aperture = 19.47
# sm.add_surface([-144.041,3,'J-LASFH2','Hikari'])      # 1.76554,46.76])    46.78
# sm.ifcs[sm.cur_surface].max_aperture = 19.14
# sm.add_surface([52.858,14.5])
# sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=52.858, cc=0,
#         coefs=[0.0,3.18645e-06,-1.14718e-08,7.74567e-11,-2.24225e-13,3.3479e-16,-1.7047e-19])
# sm.ifcs[sm.cur_surface].max_aperture = 19.14
# sm.add_surface([0,1.6,'J-BK7A', 'Hikari'])             # 1.5168,64.14
# sm.ifcs[sm.cur_surface].max_aperture = 22.15
# sm.add_surface([0,1])
# sm.ifcs[sm.cur_surface].max_aperture = 22.15

sm.list_surfaces()
sm.list_gaps()
sm.do_apertures = False
opm.update_model()
#apply_paraxial_vignetting(opm)
sm.list_model()
# List the optical specifications
pm.first_order_data()
# List the paraxial model
pm.list_lens()

# all_fields_traced_rays = rayoptics.raytr.trace.trace_all_fields(opm)

#print(all_fields_traced_rays)

layout = LensLayout(opm)

ele_model = opm.ele_model
part_tree = opm.part_tree

print('------------ elements -------------')
ele_model.list_elements()

print('------------ element model -------------')
ele_model.list_model()

rays = layout.create_ray_entities(None, 0.0)
for ray in rays:
    ray.update_shape(None)

print('done')