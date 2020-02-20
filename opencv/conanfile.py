from conans import ConanFile, CMake, tools

class OpencvConan(ConanFile):
    name = "Opencv"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    settings = {
            "os": "Linux",
            "compiler": "gcc",
            }
    options = {"shared": [True, False], "gtk": [None, 2, 3]}
    default_options = {"shared": True, "gtk": 2}
    requires = [
            "boost/1.71.0@conan/stable"
            ]
    generators = "cmake_find_package", "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()
