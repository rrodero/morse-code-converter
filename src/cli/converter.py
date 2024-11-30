import json
from typing import Dict


class Converter:
    """A class for converting text to Morse code and vice versa."""

    def __init__(self):
        """Initializes the Converter with the Morse alphabet."""
        self.morse_alphabet = {
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
            ".": ".-.-.-",
            ",": "--..--",
            "?": "..--..",
            "!": "-.-.--",
            "-": "-....-",
            "/": "-..-.",
            "@": ".--.-.",
            "(": "-.--.",
            ")": "-.--.-"
        }

    def encrypt_message(self, message: str) -> str:
        """Encrypts a given text message into Morse code.

            Args:
                message: The text message to encrypt.

            Returns:
                The encrypted Morse code.
        """
        ciphers = [self.morse_alphabet[letter] + " " if letter != " " else " " for letter in message]
        return "".join(ciphers)

    def decrypt_message(self, morse_code: str) -> str:
        """Decrypts a given Morse code into text.

            Args:
                morse_code: The Morse code to decrypt.

            Returns:
                The decrypted text.
        """
        morse_code = morse_code.replace("  ", " / ")
        print(morse_code.split())
        clear_letters = [list(self.morse_alphabet.keys())[list(self.morse_alphabet.values()).index(letter)]
                      if letter != "/" else " " for letter in morse_code.split()]
        return "".join(clear_letters)