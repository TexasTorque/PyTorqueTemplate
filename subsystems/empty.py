from lib.subsystem.TorqueSubsystem import Subsystem
import systems

class Empty(Subsystem):
    def initialize(self) -> None:
        pass

    def update(self) -> None:
        pass

_instance = None

def get_instance() -> Empty:
    global _instance
    if _instance == None:
        _instance = Empty()
    return _instance