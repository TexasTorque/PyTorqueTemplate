from lib.auto.TorqueAutoManager import TorqueAutoManager
from auto.sequences.testsequence import TestSequence

class AutoManager(TorqueAutoManager):
    def __init__(self) -> None:
        super().__init__()

    def load_paths(self) -> None:
        self.path_loader.preload_path("test")
    
    def load_sequences(self) -> None:
        self.add_sequence("Test", TestSequence())

_instance = None

def get_automanager() -> AutoManager:
    global _instance
    if _instance == None:
        _instance = AutoManager()
    return _instance