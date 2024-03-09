from lib.robot.TorqueRobot import TorqueRobotBase
import systems

class Robot(TorqueRobotBase):
    def __init__(self) -> None:
        systems.initialize()