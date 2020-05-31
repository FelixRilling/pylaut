import logging

from pylaut import PyLaut

logging.basicConfig(level=logging.INFO)

PyLaut({
    "ae;": "ä", "Ae;": "Ä",
    "oe;": "ö", "Oe;": "Ö",
    "ue;": "ü", "Ue;": "Ü",
    "ss;": "ß",
}).start()
