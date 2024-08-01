from lib.subsystem.TorqueSubsystem import TorqueSubsystem
from lib.base.TorqueMode import TorqueMode
import wpilib

class Input(TorqueSubsystem):
    def initialize(self, mode: TorqueMode) -> None:
        self.driver: wpilib.XboxController = wpilib.XboxController(0)
        self.operator: wpilib.XboxController = wpilib.XboxController(1)

    def update(self, mode: TorqueMode) -> None:
        pass

    def clean(self, mode: TorqueMode) -> None:
        pass

_instance = None

def get_input() -> Input:
    global _instance
    if _instance == None:
        _instance = Input()
    return _instance