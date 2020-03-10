from conans import ConanFile, CMake, tools

class BoostServerConan(ConanFile):
    name = "BoostServer"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    settings = {
            "os": "Linux",
            "compiler": "gcc",
            }
    requires = [
            "boost/1.71.0@conan/stable",
            "zlib/1.2.11@conan/stable",
            "opencv/4.1.1@conan/stable"
            ]
    generators = "cmake_find_package"
    options = {
        "gtk" : [None, 2, 3]
    }
    default_options = {
        "gtk": 2
    }
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
