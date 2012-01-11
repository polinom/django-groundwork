from setuptools import setup, find_packages

requires = []
setup(
    name = "django-groundwork",
    description='django command for automatic generation basic cod for app',
    version = "0.1",
    author = "Polynrts Igor, krisys, Madhusudan.C.S, stac",
    packages = find_packages("src", exclude=["*.tests", "*.tests.*",
                                              "tests.*", "tests"]),
    package_dir = {'':'src'},
    install_requires = requires,
    tests_require = requires
  )

