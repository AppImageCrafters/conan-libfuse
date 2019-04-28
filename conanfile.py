from conans import ConanFile, AutoToolsBuildEnvironment, tools


class SquashfuseConan(ConanFile):
    name = "fuse"
    version = "2.9.9"
    license = "https://github.com/libfuse/libfuse/blob/master/LICENSE"
    author = "Alexis Lopez Zubieta <contact@azubieta.net>"
    url = "https://github.com/appimage-conan-community/conan-libfuse"
    description = "libfuse conan package for AppImage "
    topics = ("fuse")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    def source(self):
        tools.download("https://github.com/libfuse/libfuse/releases/download/fuse-2.9.9/fuse-2.9.9.tar.gz",
                       "fuse-2.9.9.tar.gz")
        tools.untargz("fuse-2.9.9.tar.gz")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.fpic = True
        env_build_vars = autotools.vars
        autotools.configure(configure_dir="fuse-2.9.9", vars=env_build_vars,
                            args=["--disable-util", "--disable-example", "--verbose", ])
        autotools.make(vars=env_build_vars)
        autotools.install(vars=env_build_vars)

    def package_info(self):
        self.cpp_info.libs = ["fuse"]
        self.cpp_info.builddirs = ["lib/pkgconfig/"]
        self.cpp_info.defines = ["_FILE_OFFSET_BITS=64"]
