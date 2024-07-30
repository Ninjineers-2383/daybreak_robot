import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import xacro


def generate_launch_description():

    # Check if we're told to use sim time
    sim = LaunchConfiguration('sim')


    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('daybreak_robot'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')

    robot_description = Command(['xacro ', xacro_file, ' sim:=', sim])

    
    # Create a robot_state_publisher node
    params = {'robot_description': robot_description, 'use_sim_time': sim}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )


    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'sim',
            default_value='false',
            description='Sim mode'),

        node_robot_state_publisher
    ])
