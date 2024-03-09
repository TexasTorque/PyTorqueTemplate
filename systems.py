from input import Input
from subsystems.empty import Empty
from lib.subsystem.TorqueSubsystem import Subsystem

subsystems: list[Subsystem] = []

def add_subsystems() -> None:
    # Add subsystems here
    subsystems.append(Empty())
    subsystems.append(Input())

    for subsystem in subsystems:
        subsystem.set_subsystems(subsystems)

def init_subsystems() -> None:
    for subsystem in subsystems:
        subsystem.initialize()

def update_subsystems() -> None:
    for subsystem in subsystems:
        subsystem.update()