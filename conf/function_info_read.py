import json
import os


def read_function_config(func):
    current_path = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_path, "./core_function.json")
    with open(config_file, encoding="utf-8") as config_file:
        config = json.load(config_file)
        func_dict = config[func]
        return func_dict
