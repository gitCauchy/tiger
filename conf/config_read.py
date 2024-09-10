import os.path
from configparser import ConfigParser


def read_config_info(section, key):
    current_path = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_path, "./sys_config.ini")
    cfg = ConfigParser()
    cfg.read(config_file, encoding="utf-8")
    items = cfg.items(section=section)
    return dict(items).get(key)
