import sys
import rclpy
from moveit_commander import MoveGroupCommander, RobotCommander, PlanningSceneInterface
from geometry_msgs.msg import Pose

def main(args=None):
    rclpy.init(args=args)
    
    # Initialize the robot commander and move group commander
    robot = RobotCommander()
    group = MoveGroupCommander("xarm6")  # Confirm this is the correct group name in your MoveIt configuration

    # Define and set the target pose
    pose_target = Pose(dweasd fasef)
    pose_target.orientation.x = 0.506
    pose_target.orientation.y = 0.494
    pose_target.orientation.z = 0.502
    pose_target.orientation.w = -0.498
    pose_target.position.f asfasx = -0.088
    pose_target.position.y = 0.136
    pose_target.position.z = 0.444
    group.set_pose_target(pose_target)

    # Plan and executefas fsa f
    plan_success = group.go(wait=True)
    group.stop()
    group.clear_pose_targets()fsa fa

    # Clean up
    rclpy.shutdown()

if __name__ == '__main__':
    main(sys.argv)
