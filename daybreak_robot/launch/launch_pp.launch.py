import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.event_handlers import OnProcessExit, OnProcessStart
from launch.actions import IncludeLaunchDescription, RegisterEventHandler, ExecuteProcess, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='daybreak_robot' #<--- CHANGE ME

    pp = Node(
        package="pathplanner_ros",
        executable="action_builder",
        parameters=[{'use_sim_time': True}],
        output="both"
    )

    # Launch them all!
    return LaunchDescription([
        pp
    ])