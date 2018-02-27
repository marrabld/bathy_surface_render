# Recorded script from Mayavi2
from numpy import array
try:
    engine = mayavi.engine
except NameError:
    from mayavi.api import Engine
    engine = Engine()
    engine.start()
if len(engine.scenes) == 0:
    engine.new_scene()
# ------------------------------------------- 
scene = engine.scenes[0]
scene.scene.camera.position = [1691.9007278050228, 2671.8708421559622, 1815.9457694178461]
scene.scene.camera.focal_point = [-0.5, -0.5, -120.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.053359987648918916, -0.56344712835571031, 0.82442710124413709]
scene.scene.camera.clipping_range = [9.1189154382997302, 9118.9154382997294]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [1277.3438199846444, 1957.9975528844768, 2758.3805639073798]
scene.scene.camera.focal_point = [-0.5, -0.5, -120.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.18033189282214368, -0.77413467007856485, 0.60679149714999669]
scene.scene.camera.clipping_range = [425.04070220768062, 7850.8572684883784]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [1344.1963006857557, 393.99927707946563, 3313.6328200483281]
scene.scene.camera.focal_point = [-0.5, -0.5, -120.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.35997407292981498, -0.90037593759198431, 0.24442143486952053]
scene.scene.camera.clipping_range = [1820.3833781474623, 6094.4083221420751]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
