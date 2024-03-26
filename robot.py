from lib.robot.TorqueRobot import TorqueRobotBase
import systems

class Robot(TorqueRobotBase):
    def __init__(self) -> None:
        self.add_subsystem(systems.inputsystem)
        self.add_subsystem(systems.emptysystem)