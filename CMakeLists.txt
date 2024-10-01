cmake_minimum_required(VERSION 3.5)
project(mecanum_bot)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(gazebo_ros REQUIRED)

install(PROGRAMS
  mecanum_bot/mecanum_controller.py
  launch/mecanum_bot_launch.py
  launch/view_bot_launch.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
