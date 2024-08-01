from lib.auto.TorqueSequence import TorqueSequence
from lib.auto.command.TorqueRun import TorqueRun
from lib.auto.command.TorqueWait import TorqueWait
from lib.auto.command.TorqueFollowPath import TorqueFollowPath
import systems

class TestSequence(TorqueSequence):
    def __init__(self) -> None:
        super().__init__()

        # self.add_block(TorqueRun(lambda: print("ran!")))
        # self.add_block(TorqueRun(lambda: systems.drivebase.set_speeds(3, 0, 0)))
        # self.add_block(TorqueWait(2))
        # self.add_block(TorqueRun(lambda: systems.drivebase.set_speeds(0, 0, 0)))
        # self.add_block(TorqueFollowPath("test"))