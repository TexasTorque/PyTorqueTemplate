from input import Input
from subsystems.empty import Empty
from lib.subsystem.TorqueSubsystem import Subsystem

subsystems: list[Subsystem] = []

def initialize() -> None:
    # Add subsystems here
    subsystems.append(Empty())
    subsystems.append(Input())

    for subsystem in subsystems:
        subsystem.set_subsystems(subsystems)