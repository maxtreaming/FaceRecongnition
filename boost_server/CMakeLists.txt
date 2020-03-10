cmake_minimum_required(VERSION 3.10.2)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_COMPILER g++)

project(BoostServer CXX)

find_package(boost 1.71.0 REQUIRED)
find_package(opencv 4.1.1 REQUIRED)
find_package(GTK2 REQUIRED)
find_package(Threads REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME}
    PUBLIC
    ${GTK2_LIBRARIES}
    boost::boost
    opencv::opencv
    Threads::Threads
)
