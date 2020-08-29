import logging
from typing import Dict

import yaml

from pylaut import PyLaut

logging.basicConfig(level=logging.INFO)

with open(r"./config.yaml") as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

    bindings: Dict[str, str] = config.get("bindings")
    if bindings is None:
        raise ValueError("'bindings' was not found in config.")

    PyLaut(bindings).start()
