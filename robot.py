from lib.base.TorqueRobotBase import TorqueRobotBase
import systems
import input

class Robot(TorqueRobotBase):
    def __init__(self) -> None:
        super().__init__(input.get_instance())
        self.add_subsystem(systems.empty)