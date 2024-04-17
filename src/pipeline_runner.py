import os
import sys
from pathlib import Path
from config import GlobalConfig
import importlib


sys.path.append(str(GlobalConfig.HOME_PATH))


def download():
    for data_source in GlobalConfig.EXTRACTORS:
        parts = data_source.split('.')
        module_path = '.'.join(parts[:-1])
        class_name = parts[-1]

        try:
            abs_path = os.path.abspath(__file__)
            root_path = os.path.dirname(os.path.abspath(__file__))
            relative_path = os.path.relpath(abs_path, root_path)
            print(root_path)
            module = importlib.import_module(module_path)
            class_obj = getattr(module, class_name)
            print(class_obj.__name__)
        except ImportError:
            print(f"Module '{module_path}' not found.")
        except AttributeError:
            print(f"Class '{class_name}' not found in module '{module_path}'.")


download()
