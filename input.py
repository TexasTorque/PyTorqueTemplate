from lib.subsystem.TorqueSubsystem import Subsystem
import wpilib
import systems

class Input(Subsystem):
    def initialize(self) -> None:
        self.driver: wpilib.XboxController = wpilib.XboxController(0)
        self.operator: wpilib.XboxController = wpilib.XboxController(1)

    def update(self) -> None:
        systems

_instance = None

def get_instance() -> Input:
    global _instance
    if _instance == None:
        _instance = Input()
    return _instance