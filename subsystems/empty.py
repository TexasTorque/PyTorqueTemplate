from lib.subsystem.TorqueSubsystem import TorqueSubsystem
from lib.base.TorqueMode import TorqueMode

class Empty(TorqueSubsystem):
    def initialize(self, mode: TorqueMode) -> None:
        pass

    def update(self, mode: TorqueMode) -> None:
        pass

_instance = None

def get_empty() -> Empty:
    global _instance
    if _instance == None:
        _instance = Empty()
    return _instance