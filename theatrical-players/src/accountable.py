import importlib
import os
from importlib.util import module_from_spec, spec_from_file_location
from typing import Type

from accountables.core import PlayAccountable
from models import PlayType

ACCOUNTABLES: dict[PlayType, Type[PlayAccountable]] = dict()


def add_plugin(name: PlayType, accountable: Type[PlayAccountable]) -> None:
    """Adds a plugin."""
    ACCOUNTABLES[name] = accountable


def get_plugin(name: PlayType) -> Type[PlayAccountable]:
    """Gets a plugin by name."""
    return ACCOUNTABLES[name]


def plugin_exists(name: PlayType) -> bool:
    """Checks if a plugin exists."""
    return name in ACCOUNTABLES


def all_plugins() -> list[str]:
    """Gets all plugin names."""
    return list(ACCOUNTABLES.keys())


def import_module(name: str, path: str):
    """Imports a module from a file."""
    spec = spec_from_file_location(name, path)
    if spec:
        module = module_from_spec(spec)  # type: ignore
        spec.loader.exec_module(module)  # type: ignore
        return module
    raise ImportError(f"Could not import {name} from {path}")


def load_plugins_from_folder(folder: str) -> None:
    """Loads all modules from a folder."""
    for root, _, files in os.walk(folder):
        for file in files:
            if not file.endswith(".py") or file.startswith("core"):
                continue
            module_name = file[:-3]
            module_path = os.path.join(root, file)
            module = import_module(module_name, module_path)
            account_class = getattr(module, module_name.title())
            ACCOUNTABLES[module.get_play_accountable_name()] = account_class
