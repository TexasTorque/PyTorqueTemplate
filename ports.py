class SwervePorts:
    def __init__(self, driveID: int, turnID: int, encoderID: int) -> None:
        self.driveID = driveID
        self.turnID = turnID
        self.encoderID = encoderID

class Ports:
    MOTOR: int = 5