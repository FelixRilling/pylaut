import logging
from collections import deque
from logging import Logger
from typing import Dict

from pynput import keyboard


class PyLaut:
	__logger: Logger = logging.getLogger("PyLaut")

	__key_binds: Dict[str, str]
	__key_strokes: deque
	__controller: keyboard.Controller

	def __init__(self, key_binds: Dict[str, str]):
		self.__key_binds = key_binds

		deque_max_size: int = max(map(lambda key: len(key), key_binds.keys()))
		self.__key_strokes = deque({}, deque_max_size)
		self.__logger.debug("Allocated %s slot(s) for keys in the key stroke dequeue.",
							deque_max_size)

		self.__controller = keyboard.Controller()

	def start(self):
		with keyboard.Listener(on_press=self.__on_press) as listener:
			self.__logger.info("Started listing for key inputs with %s key sequence(s) registered.",
							   len(self.__key_binds))
			listener.join()

	def __on_press(self, key: keyboard.KeyCode):
		if hasattr(key, "char") and key.char is not None:
			self.__logger.debug("Received char key %s.", key)
			self.__key_strokes.append(key.char)
			self.__check_key_binds()
		else:
			self.__logger.debug("Received non-char key %s, skipping.", key)

	def __check_key_binds(self):
		key_stroke_string: str = "".join(self.__key_strokes)
		for key_bind, key_bind_result in self.__key_binds.items():
			if key_stroke_string.endswith(key_bind):
				self.__logger.debug("Key bind '%s' was matched in key strokes '%s'!", key_bind,
									key_stroke_string)
				self.__handle_key_bind_invocation(key_bind, key_bind_result)
				break
			else:
				self.__logger.debug("Key bind '%s' was not matched in key strokes '%s'.", key_bind,
									key_stroke_string)

	def __handle_key_bind_invocation(self, key_bind: str, key_bind_result: str):
		self.__key_strokes.clear()

		# Delete inputted key sequence trigger values
		to_remove: int = len(key_bind)
		for i in range(to_remove):
			self.__controller.press(keyboard.Key.backspace)
			self.__controller.release(keyboard.Key.backspace)
		self.__logger.debug("Successfully removed %s characters of the original key bind.",
							to_remove)

		# Insert replacement
		for letter in key_bind_result:
			letter_key_code = keyboard.KeyCode.from_char(letter)
			self.__controller.press(letter_key_code)
			self.__controller.release(letter_key_code)
		self.__logger.debug("Successfully inserted key bind result '%s'.", key_bind_result)
