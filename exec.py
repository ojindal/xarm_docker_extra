import sys
import rclpy
from moveit_py.planning_component import PlanningComponent
from moveit_py.robot_model_loader import RobotModelLoader
from geometry_msgs.msg import Pose

def main(args=None):
    rclpy.init(args=args)
    
    # Load the robot model
    robot_model_loader = RobotModelLoader("robot_description")
    robot_model = robot_model_loader.get_model()

    # Initialize the planning component with the group name
    arm_group_name = "xarm6"  # Confirm this is the correct group name in your MoveIt configuration
    planner = PlanningComponent(arm_group_name, robot_model)

    # Define and set the target pose
    pose_target = Pose()
    pose_target.orientation.x = 0.506
    pose_target.orientation.y = 0.494
    pose_target.orientation.z = 0.502
    pose_target.orientation.w = -0.498
    pose_target.position.x = -0.088
    pose_target.position.y = 0.136
    pose_target.position.z = 0.444
    planner.set_pose_target(pose_target)

    # Plan and execute
    plan_success, motion_plan = planner.plan()
    if plan_success:
        planner.execute(motion_plan)

    # Clean up
    rclpy.shutdown()

if __name__ == '__main__':
    main(sys.argv)
