cmake_minimum_required(VERSION 3.10.2)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_COMPILER g++)

project(helloworld CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)


add_executable(helloworld hello.cpp)

target_link_libraries(helloworld
    PUBLIC
    CONAN_PKG::opencv)
