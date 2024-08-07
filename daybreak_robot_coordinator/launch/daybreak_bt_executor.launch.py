import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import xacro


def generate_launch_description():

    # Check if we're told to use sim time
    sim = LaunchConfiguration('use_sim_time')


    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('daybreak_robot_coordinator'))

    
    # Create a robot_state_publisher node
    params = {'use_sim_time': sim}
    node_robot_state_publisher = Node(
        package='daybreak_robot_coordinator',
        executable='daybreak_bt_executor',
        output='screen',
        parameters=[params, os.path.join(pkg_path, 'config', 'daybreak_bt_executor.yaml')]
    )


    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='use sim time'),

        node_robot_state_publisher
    ])
