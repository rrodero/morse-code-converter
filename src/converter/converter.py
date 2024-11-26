import json

class Converter():

    def __init__(self):
        self.morse_alphabet = self.load_alphabet()


    def load_alphabet(self) -> dict[str, str]:
        with open("../../resources/morse.json") as morse_json:
            return json.load(morse_json)


    def encrypt_message(self, message: str) -> str:
        ciphers = [self.morse_alphabet[letter] + ' ' if letter != ' ' else ' ' for letter in message]
        return ''.join(ciphers)