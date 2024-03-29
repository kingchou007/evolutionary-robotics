import pybullet as p
import pybullet_data
import constants as c


class WORLD:
    def __init__(self):
        # self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.gravity)
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
