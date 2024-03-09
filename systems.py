from input import Input
from subsystems.empty import Empty
from lib.subsystem.TorqueSubsystem import Subsystem

subsystems: list[Subsystem] = []

# Define subsystems here
empty = Empty()
subsystems.append(empty)
input = Input()
subsystems.append(input)

for subsystem in subsystems:
    subsystem.set_subsystems(subsystems)