import json


def load_alphabet() -> dict[str, str]:
    with open("../../resources/morse.json") as morse_json:
        return json.load(morse_json)


class Converter:

    def __init__(self):
        self.morse_alphabet = load_alphabet()

    def encrypt_message(self, message: str) -> str:
        ciphers = [self.morse_alphabet[letter] + " " if letter != " " else " " for letter in message]
        return "".join(ciphers)

    def decrypt_message(self, morse_code: str) -> str:
        morse_code = morse_code.replace("  ", " / ")
        print(morse_code.split())
        clear_letters = [list(self.morse_alphabet.keys())[list(self.morse_alphabet.values()).index(letter)]
                      if letter != "/" else " " for letter in morse_code.split()]
        return "".join(clear_letters)