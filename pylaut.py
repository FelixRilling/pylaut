from collections import deque
from typing import Union, Dict

from pynput import keyboard
from pynput.keyboard import Controller, KeyCode, Key


class PyLaut:
    __key_map: Dict[str, str]
    __key_strokes: deque

    def __init__(self, key_map: Dict[str, str]):
        self.__key_map = key_map
        deque_max_size: int = max(key_map.keys(), key=str.__len__).__len__()
        self.__key_strokes = deque({}, deque_max_size)

    def start(self):
        with keyboard.Listener(
                on_press=self.__on_press) as listener:
            listener.join()

        listener.start()

    def __on_press(self, key: keyboard.KeyCode):
        if hasattr(key, "char") and key.char is not None:
            self.__key_strokes.append(key.char)
            key_stroke_string: str = "".join(self.__key_strokes)
            for sequence, target in self.__key_map.items():
                if key_stroke_string.endswith(sequence):
                    self.__handle_binding_invocation(sequence, target)
                    break

    def __handle_binding_invocation(self, sequence: str, target: str):
        controller: Union[Controller, Controller, Controller, Controller] = keyboard.Controller()
        self.__key_strokes.clear()
        for i in range(len(sequence)):
            controller.press(Key.backspace)
            controller.release(Key.backspace)
        for letter in target:
            letter_key_code = KeyCode.from_char(letter)
            controller.press(letter_key_code)
            controller.release(letter_key_code)
