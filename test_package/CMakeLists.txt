cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)
set(CMAKE_CXX_STANDARD 11)

find_package(PkgConfig)
pkg_check_modules(fuse REQUIRED IMPORTED_TARGET fuse)

add_executable(example example.cpp)
target_link_libraries(example PkgConfig::fuse)
