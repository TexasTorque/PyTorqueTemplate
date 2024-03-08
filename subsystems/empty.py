from lib.subsystem import Subsystem

class Empty(Subsystem):
    def __init__(self) -> None:
        super().__init__("Empty")
    
    def initialize(self) -> None:
        pass

    def update(self) -> None:
        pass