cmake_minimum_required(VERSION 3.5)
project(lr_interfaces)

# Default to C++14 (or keep C++11 if preferred)
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14) # 或者使用 11
endif()
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Generate messages and services
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/Height.srv"
  DEPENDENCIES builtin_interfaces
)

# Export include directories for this package
ament_export_include_directories(include)

# Export dependencies
ament_export_dependencies(rosidl_default_runtime)

# Install rules
install(
  DIRECTORY include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME}
)

# 安装服务文件
install(
  DIRECTORY srv/
  DESTINATION share/${PROJECT_NAME}/srv
)

ament_package()