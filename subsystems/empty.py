from lib.subsystem.TorqueSubsystem import TorqueSubsystem
import systems

class Empty(TorqueSubsystem):
    def initialize(self, mode) -> None:
        pass

    def update(self, mode) -> None:
        pass

_instance = None

def get_instance() -> Empty:
    global _instance
    if _instance == None:
        _instance = Empty()
    return _instance