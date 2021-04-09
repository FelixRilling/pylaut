import argparse
import logging
from typing import Dict

import yaml

from pylaut import PyLaut

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(
    description="Simple Python script allowing for key sequence input triggered text replacement."
)
parser.add_argument(
    "-c",
    "--config",
    default=r"./config.yaml",
    help="path to a configuration file."
)
args = parser.parse_args()

logging.debug("Loading config '%s'.", args.config)
with open(args.config, encoding="utf8") as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

    bindings: Dict[str, str] = config.get("bindings")
    if bindings is None:
        raise ValueError("'bindings' was not found in config.")

    PyLaut(bindings).start()
