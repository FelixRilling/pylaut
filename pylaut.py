from collections import deque
from typing import Dict

from pynput import keyboard


class PyLaut:
    __key_map: Dict[str, str]
    __key_strokes: deque
    __controller: keyboard.Controller

    def __init__(self, key_map: Dict[str, str]):
        self.__key_map = key_map
        deque_max_size: int = max(map(lambda key: len(key), key_map.keys()))
        self.__key_strokes = deque({}, deque_max_size)
        self.__controller = keyboard.Controller()

    def start(self):
        with keyboard.Listener(
                on_press=self.__on_press) as listener:
            listener.join()
        listener.start()

    def __on_press(self, key: keyboard.KeyCode):
        if hasattr(key, "char") and key.char is not None:
            self.__key_strokes.append(key.char)
            self.__check_key_binds()

    def __check_key_binds(self):
        key_stroke_string: str = "".join(self.__key_strokes)
        for sequence, target in self.__key_map.items():
            if key_stroke_string.endswith(sequence):
                self.__handle_key_bind_invocation(sequence, target)
                break

    def __handle_key_bind_invocation(self, sequence: str, target: str):
        self.__key_strokes.clear()

        # Delete inputted key map values
        for i in range(len(sequence)):
            self.__controller.press(keyboard.Key.backspace)
            self.__controller.release(keyboard.Key.backspace)

        # Input replacement
        for letter in target:
            letter_key_code = keyboard.KeyCode.from_char(letter)
            self.__controller.press(letter_key_code)
            self.__controller.release(letter_key_code)
