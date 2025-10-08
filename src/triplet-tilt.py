from rayoptics.environment import *

opm = OpticalModel()
sm  = opm.seq_model
osp = opm.optical_spec
pm = opm.parax_model

osp.pupil = PupilSpec(osp, key=['object', 'pupil'], value=12.5)
osp.field_of_view = FieldSpec(osp, key=['object', 'angle'], value=20.0, flds=[0., 0.707, 1.], is_relative=True)
osp.spectral_region = WvlSpec([('F', 0.5), ('d', 1.0), ('C', 0.5)], ref_wl=1)

opm.radius_mode = True

sm.gaps[0].thi=1e10

sm.add_surface([23.713, 4.831, 'N-LAK9', 'Schott'])
sm.add_surface([7331.288, 5.86])
sm.add_surface([-24.456, .975, 'N-SF5,Schott'])
sm.set_stop()
sm.add_surface([21.896, 4.822])
sm.add_surface([86.759, 3.127, 'N-LAK9', 'Schott'])
sm.add_surface([-20.4942, 41.2365-.11])

opm.update_model()

pm.first_order_data()

fld, wvl, foc = osp.lookup_fld_wvl_focus(0)

ray_xfan = analyses.RayFan(opm, f=fld, wl=wvl, xyfan='x')
ray_yfan = analyses.RayFan(opm, f=fld, wl=wvl, xyfan='y')
ray_grid = analyses.RayGrid(opm, f=fld, wl=wvl)


