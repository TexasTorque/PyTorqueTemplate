from wpilib import DriverStation 
from wpimath import units
from wpimath.geometry import Translation2d, Rotation2d, Pose2d
import math

alliance = DriverStation.getAlliance()
FIELD_LENGTH = 16.541
FIELD_WIDTH = units.inchesToMeters(315.5)
SPEAKER_Y = 5.55
SPEAKER_X = 0
ANGLE_TO_LASER = 60
ALLIANCE_WING_LENGTH = 6
FAR_SIDE_SPEAKER_Y = 5.2
LASER_ADJUSTMENT = 1
LASER_CHECKPOINT = 38 * LASER_ADJUSTMENT
LASER_UNDERSTAGE = 20 * LASER_ADJUSTMENT

"""
Field setup:
__________________
|     |     |     |
|     ￣￣￣￣     |
|                 |   <- FIELD LENGTH ~ 16.541m
|                 |      x-axis
|                 |    
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|     _______     |
|     |     |     |
￣￣￣￣￣￣￣￣￣￣
            ^
FIELD WIDTH ~ 8.21m   
y-axis 

"""
    
speaker_pose = Pose2d()
passing_zone = Pose2d()
normal_speaker_pose = Pose2d() 
far_side_speaker_pose = Pose2d()

def update_alliance():
    global normal_speaker_pose
    global far_side_speaker_pose

    is_red_alliance = alliance == DriverStation.Alliance.kRed
    if is_red_alliance:
        normal_speaker_pose = Pose2d(Translation2d(FIELD_LENGTH - SPEAKER_X, SPEAKER_Y), 
                                            Rotation2d().fromDegrees(0))
        far_side_speaker_pose = Pose2d(Translation2d(FIELD_LENGTH - SPEAKER_X, FAR_SIDE_SPEAKER_Y), 
                                            Rotation2d().fromDegrees(0))
    else:
        normal_speaker_pose = Pose2d(Translation2d(SPEAKER_X, SPEAKER_Y), 
                                            Rotation2d().fromDegrees(0))
        far_side_speaker_pose = Pose2d(Translation2d(SPEAKER_X, FAR_SIDE_SPEAKER_Y), 
                                            Rotation2d().fromDegrees(0))

# Set speaker pose to far side speaker  
def use_far_side_speaker(use_far_side):
    global speaker_pose

    speaker_pose = far_side_speaker_pose if use_far_side else normal_speaker_pose

# Calculated distance between poses using distance formula
def distance_between_poses(pose1: Pose2d, pose2: Pose2d):
    return math.sqrt(((pose2.Y() - pose1.Y())**2)
                    - ((pose2.X() - pose1.X())**2))

# Distance from pose to speaker
def distance_to_speaker(pose: Pose2d):
    return distance_between_poses(pose, speaker_pose)

# Get what mode
def is_teleop():
    return DriverStation.isTeleop()