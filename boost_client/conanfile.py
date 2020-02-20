from conans import ConanFile, CMake, tools

class BoostClientConan(ConanFile):
    name = "BoostClient"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    settings = {
            "os": "Linux",
            "compiler": "gcc",
            }
    requires = [
            "boost/1.71.0@conan/stable"
            ]
    generators = "cmake_find_package"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
