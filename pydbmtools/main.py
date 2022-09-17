"""
main entry point to the program
"""

import dbm.gnu
import pylogconf.core
from pytconf import register_main, config_arg_parse_and_launch, register_endpoint, get_free_args
from pydbmtools.static import DESCRIPTION, APP_NAME, VERSION_STR


@register_endpoint(
    description="List the content of a dbm file",
    configs=[],
    allow_free_args=True,
    max_free_args=2,
)
def dump() -> None:
    filename = get_free_args()[0]
    with dbm.gnu.open(filename) as db:
        key = db.firstkey()
        while key is not None:
            value = db.get(key)
            if value is not None:
                print(key.decode(), len(value), type(value))
            else:
                print(key.decode(), type(value))
            key = db.nextkey(key)


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
