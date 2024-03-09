import wpilib
from lib.subsystem.TorqueSubsystem import Subsystem
from ports import Ports

class Input(Subsystem):
    def __init__(self) -> None:
        super().__init__("Input")
        self.driver: wpilib.XboxController = wpilib.XboxController(0)
        self.operator: wpilib.XboxController = wpilib.XboxController(1)
    
    def initialize(self) -> None:
        pass

    def update(self) -> None:
        pass