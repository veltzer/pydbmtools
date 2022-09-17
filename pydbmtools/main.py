"""
main entry point to the program
"""

import pylogconf.core
from pytconf import register_main, config_arg_parse_and_launch, register_endpoint
from pydbmtools.static import DESCRIPTION, APP_NAME, VERSION_STR


@register_endpoint(
    description="List the content of a dbm file",
    configs=[]
)
def dump() -> None:
    pass


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
