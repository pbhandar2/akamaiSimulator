cmake_minimum_required (VERSION 2.8)

project (akamaiSimulator)
set (akamaiSimulator_VERSION_MAJOR 0)
set (akamaiSimulator_VERSION_MINOR 1)
set (akamaiSimulator_VERSION_REVISION 0)


# add_compile_options(-std=c++11)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")


# header
include_directories(src/include)
include_directories(src/libketama/include)
include_directories(src/utils/include)
include_directories(CMimircache/CMimircache/headers)
include_directories(CMimircache/CMimircache/cache/include)
include_directories(CMimircache/CMimircache/cacheReader/include)
include_directories(CMimircache/CMimircache/dataStructure/include)
include_directories(CMimircache/CMimircache/profiler/include)
include_directories(CMimircache/CMimircache/utils/include)


set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/CMimircache/CMimircache/cmake/Modules/")
message(STATUS ${CMAKE_MODULE_PATH})

# set CXX options
SET(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
SET(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")


# find lib
find_package(GLib "2.40" REQUIRED)
include_directories(${GLib_INCLUDE_DIRS})
set(LIBS ${LIBS} ${GLib_LIBRARY})
message(STATUS "gLib found? " ${GLib_FOUND})
message(STATUS "LIBS = " ${LIBS})
message(STATUS "GLib header = " ${GLib_INCLUDE_DIRS})


aux_source_directory(src dirAkamaiSimulator)
message(STATUS "akamaiSimulator sources = " ${dirAkamaiSimulator})


add_subdirectory(CMimircache/CMimircache/cache)
add_subdirectory(CMimircache/CMimircache/cacheReader)
add_subdirectory(CMimircache/CMimircache/dataStructure)
add_subdirectory(CMimircache/CMimircache/profiler)
add_subdirectory(CMimircache/CMimircache/utils)

add_subdirectory(src/libketama)


# executable
add_executable(akamaiSimulatorBin ${dirAkamaiSimulator})

# link library
target_link_libraries(akamaiSimulatorBin libketama cache cacheReader dataStructure profiler utils m ${LIBS} ${CMAKE_THREAD_LIBS_INIT} -lpthread)






# mkdir build
# cd    build
# rm -r *; cmake .. -G Ninja; ninja
# cmake ..; make -j12


# cmake -DCMAKE_BUILD_TYPE=Debug ..
# cmake -DCMAKE_BUILD_TYPE=Release ..