"""
All configurations
"""
from pytconf import Config, ParamCreator


class ConfigPrint(Config):
    """ How to dump things """
    full = ParamCreator.create_bool(
        help_string="full dumps or just id?",
        default=False,
    )
