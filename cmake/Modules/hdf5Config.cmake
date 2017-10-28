INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_HDF5 hdf5)

FIND_PATH(
    HDF5_INCLUDE_DIRS
    NAMES hdf5/api.h
    HINTS $ENV{HDF5_DIR}/include
        ${PC_HDF5_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    HDF5_LIBRARIES
    NAMES gnuradio-hdf5
    HINTS $ENV{HDF5_DIR}/lib
        ${PC_HDF5_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(HDF5 DEFAULT_MSG HDF5_LIBRARIES HDF5_INCLUDE_DIRS)
MARK_AS_ADVANCED(HDF5_LIBRARIES HDF5_INCLUDE_DIRS)

