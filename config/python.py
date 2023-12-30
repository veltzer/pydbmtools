from typing import List


console_scripts: List[str] = [
    "pydbmtools=pydbmtools.main:main",
]
dev_requires: List[str] = [
    "pypitools",
    "black",
]
config_requires: List[str] = []
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
]
make_requires: List[str] = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires: List[str] = [
    "pytest",
    "pytest-cov",
    "pylint",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
