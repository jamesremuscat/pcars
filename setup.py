from setuptools import setup, find_packages
import re
import sys

VERSIONFILE = "src/pcars/_version.py"
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
except EnvironmentError:
    print("unable to find version in %s" % (VERSIONFILE,))
    raise RuntimeError("if %s exists, it is required to be well-formed" % (VERSIONFILE,))

install_requires = ["binio"]
if sys.version_info < (3, 4):
    install_requires.append("enum34")

setup(
    name="pcars",
    version=verstr,
    description="Project CARS UDP feed client",
    author="James Muscat",
    author_email="jamesremuscat@gmail.com",
    url="https://github.com/jamesremuscat/pcars",
    packages=find_packages("src", exclude=["*.tests"]),
    package_dir={"": "src"},
    long_description="""
      pcars is a Python client for Project CARS's UDP data feed.
      """,
    setup_requires=["nose>=1.0"],
    tests_require=[],
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
        ],
    }
)
