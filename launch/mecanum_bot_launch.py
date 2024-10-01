import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='gzserver',
            output='screen',
            arguments=['-s', 'libgazebo_ros_factory.so']
        ),
        Node(
            package='gazebo_ros',
            executable='gzclient',
            output='screen'
        ),
        Node(
            package='mecanum_bot',
            executable='spawn_entity.py',
            arguments=['-entity', 'mecanum_bot', '-file', os.path.join(get_package_share_directory('mecanum_bot'), 'urdf', 'mecanum_bot.urdf')]
        )
    ])
