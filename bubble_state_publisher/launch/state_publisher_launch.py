'''
Author: Ligcox
Date: 2022-07-11 18:20:01
FilePath: /bubble/src/bubble_navigation/bubble_state_publisher/launch/state_publisher_launch.py
LastEditors: Ligcox
LastEditTime: 2022-07-13 03:36:27
License: GNU General Public License v3.0. See LICENSE file in root directory.
Copyright (c) 2022 Birdiebot R&D Department
Shanghai University Of Engineering Science. All Rights Reserved
'''
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, EmitEvent, RegisterEventHandler
from launch.conditions import IfCondition, UnlessCondition
from launch.event_handlers import OnProcessExit
from launch.events import Shutdown
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node


def generate_launch_description():
    urdf_file_name = 'sentryup.urdf'
    urdf = os.path.join(get_package_share_directory(
        'bubble_state_publisher'), urdf_file_name)

    return LaunchDescription([
        DeclareLaunchArgument(
            "urdf_file_path",
            default_value=urdf,
            description="Robot descript urdf model absolute path."
        ),

        Node(
            package='bubble_state_publisher',
            executable='state_publisher',
            name='state_publisher',
            output='screen',
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('urdf_file_path')])}]
        ),
    ])
