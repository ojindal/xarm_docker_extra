import sys
import rclpy
from moveit2 import MoveIt2Interface
from geometry_msgs.msg import Pose

def main(args=None):
    rclpy.init(args=args)
    moveit2 = MoveIt2Interface()

    # Define the planning group for the xArm6
    arm_group_name = "xarm6"  # Confirm this is the correct group name in your MoveIt configuration
    moveit2.setup_group(arm_group_name)

    # Set target pose with specific coordinates
    pose_target = Pose()
    pose_target.orientation.x = 0.506
    pose_target.orientation.y = 0.494
    pose_target.orientation.z = 0.502
    pose_target.orientation.w = -0.498
    pose_target.position.x = -0.088
    pose_target.position.y = 0.136
    pose_target.position.z = 0.444
    moveit2.set_pose_target(pose_target)

    # Plan and execute
    success = moveit2.go(wait=True)
    moveit2.stop()

    # Clean up
    moveit2.dispose()
    rclpy.shutdown()

if __name__ == '__main__':
    main(sys.argv)
