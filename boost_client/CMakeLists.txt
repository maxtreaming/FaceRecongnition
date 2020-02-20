cmake_minimum_required(VERSION 3.10.2)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_COMPILER g++)

project(BoostClient CXX)

find_package(boost 1.71.0 REQUIRED)
add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME}
    PUBLIC
    boost::boost)
