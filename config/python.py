console_scripts = [
    "pydbmtools=pydbmtools.main:main",
]
dev_requires = [
    "pypitools",
    "black",
]
config_requires = []
install_requires = [
    "pytconf",
    "pylogconf",
]
make_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires = [
    "pytest",
    "pytest-cov",
    "pylint",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
