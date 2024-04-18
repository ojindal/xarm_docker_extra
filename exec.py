import sys
import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import rospy

def move_to_position(x, y, z):
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface', anonymous=True)

    # Instantiate a RobotCommander object
    robot = moveit_commander.RobotCommander()

    # Instantiate a PlanningSceneInterface object
    scene = moveit_commander.PlanningSceneInterface()

    # Instantiate a MoveGroupCommander object, which is an interface to one group of joints
    group = moveit_commander.MoveGroupCommander("xarm6")

    # Create a PoseStamped message with the desired position and orientation
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.x = 0.506
    pose_target.orientation.y = 0.494
    pose_target.orientation.z = 0.502
    pose_target.orientation.w = -0.498
    pose_target.position.x = x
    pose_target.position.y = y
    pose_target.position.z = z

    # Set the target pose
    group.set_pose_target(pose_target)

    # Plan and execute the motion
    plan = group.plan()
    group.go(wait=True)

    # Calling `stop()` ensures that there is no residual movement
    group.stop()
    group.clear_pose_targets()

    # Shutdown MoveIt cleanly
    moveit_commander.roscpp_shutdown()

# Example usage
if __name__ == '__main__':
    # Coordinates for the desired position
    move_to_position(-0.088, 0.136, 0.444)
