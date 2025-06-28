""" python deps for this project """

console_scripts: list[str] = [
    "pydbmtools=pydbmtools.main:main",
]
config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "pytconf",
    "pylogconf",
]
build_requires: list[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: list[str] = [
    "pytest",
    "pytest-cov",
    "pylint",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
