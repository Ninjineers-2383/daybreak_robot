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
    tf_prefix = LaunchConfiguration('tf_prefix')
    name = LaunchConfiguration('name')


    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('daybreak_robot'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')

    # with open(xacro_file, 'r') as infp:
    #     robot_description = infp.read()

    robot_description = Command(['xacro ', xacro_file, ' sim:=', sim])

    
    # Create a robot_state_publisher node
    params = {'robot_description': robot_description, 'use_sim_time': sim, 'frame_prefix': tf_prefix}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name=name,
        output='screen',
        parameters=[params]
    )


    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'sim',
            default_value='false',
            description='Sim mode'),
        DeclareLaunchArgument(
            'tf_prefix',
            default_value='',
            description='TF Prefix'),
        DeclareLaunchArgument(
            'name',
            default_value='robot_state_publisher',
            description='Node Name'),

        node_robot_state_publisher
    ])
