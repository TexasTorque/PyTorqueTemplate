import wpilib

from lib.subsystem import Subsystem
from subsystems.empty import Empty

class PyCorliss(wpilib.TimedRobot):
    subsystems: list[Subsystem] = []

    empty: Empty

    def robotInit(self) -> None:
        # Define and add subsystems
        self.empty = Empty()
        self.subsystems.append(self.empty)

        # Define controller(s)
        self.driver = wpilib.XboxController(0)

        # Run initialize function in all subsystems
        for subsystem in self.subsystems:
            subsystem.initialize()

    def teleopPeriodic(self) -> None:
        # Add all input from controller updates here

        # Update all subsystems
        for subsystem in self.subsystems:
            subsystem.update()

    def autoInit(self) -> None:
        pass

    def autoPeriodic(self) -> None:
        pass

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass