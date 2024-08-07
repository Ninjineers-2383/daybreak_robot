cmake_minimum_required(VERSION 3.8)
project(daybreak_robot_coordinator)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
set(THIS_PACKAGE_DEPS
  behaviortree_ros2
  std_msgs
  std_srvs
  btcpp_ros2_interfaces
)

foreach(Dependency IN ITEMS ${THIS_PACKAGE_DEPS})
  find_package(${Dependency} REQUIRED)
endforeach()


add_executable(daybreak_bt_executor src/daybreak_robot_coordinator.cpp)
ament_target_dependencies(daybreak_bt_executor ${THIS_PACKAGE_DEPS})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(TARGETS
  daybreak_bt_executor
  DESTINATION lib/${PROJECT_NAME}
)

######################################################
# INSTALL plugins for other packages to load

# install(TARGETS
#   sleep_plugin
#   LIBRARY DESTINATION share/${PROJECT_NAME}/bt_plugins
#   ARCHIVE DESTINATION share/${PROJECT_NAME}/bt_plugins
#   RUNTIME DESTINATION share/${PROJECT_NAME}/bt_plugins
# )

######################################################
# INSTALL ROS config and launch files

install(DIRECTORY
    config
    launch
    DESTINATION share/${PROJECT_NAME}/
  )


ament_export_dependencies(behaviortree_ros2 btcpp_ros2_interfaces)

ament_package()
