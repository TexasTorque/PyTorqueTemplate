from lib.base.TorqueRobotBase import TorqueRobotBase
import systems
import input

class Robot(TorqueRobotBase):
    def __init__(self) -> None:
        super().__init__()

        self.set_input(input.get_input())
        
        self.add_subsystem(systems.empty)