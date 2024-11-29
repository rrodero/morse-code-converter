from typing import Optional
import typer
from typing_extensions import Annotated

from src.cli.converter import Converter

app = typer.Typer(rich_markup_mode="rich", no_args_is_help=True)

converter = Converter()


def process_file(file_path: str, process_func):
    """Processes the content of a file line by line.

        Args:
            file_path: The path to the file.
            process_func: The function to apply to each line.

        Returns:
            The processed text.
    """
    try:
        with open(file_path, "r") as file:
            return "".join(process_func(line) for line in file)
    except FileNotFoundError:
        print(f"Input file '{file_path}' not found.")
        raise typer.Exit(code=1)


@app.command()
def encrypt(text: Annotated[Optional[str], typer.Argument(help="Text to be encrypted to morse code")] = None,
            input_file: Annotated[str, typer.Option("--input", "-i", help="Specify the input file")] = None,
            output_file: Annotated[str, typer.Option("--output", "-o", help="Specify the output file")] = None):

    """Encrypts the given text or file content to Morse code."""

    if text:
        morse_code = converter.encrypt_message(text)
    elif input_file:
        morse_code = process_file(input_file, converter.encrypt_message)
    else:
        print("No text or input file provided for encryption.")
        raise typer.Abort()

    if output_file:
        with open(output_file, "w") as output_file:
            output_file.write(morse_code)
    else:
        print(morse_code)


@app.command()
def decrypt(morse_code: Annotated[Optional[str], typer.Argument(help="Morse code to be decrypted to clear text")] = None,
            input_file: Annotated[str, typer.Option("--input", "-i", help="Specify the input file")] = None,
            output_file: Annotated[str, typer.Option("--output", "-o", help="Specify the output file")] = None):
    """Decrypts the given Morse code or file content to text."""
    if morse_code:
        text = converter.decrypt_message(morse_code)
    elif input_file:
        text = process_file(input_file, converter.decrypt_message)
    else:
        print("No Morse code or input file provided for decryption.")
        raise typer.Abort()

    if output_file:
        with open(output_file, "w") as output_file:
            output_file.write(text)
    else:
        print(text)


if __name__ == "__main__":
    app()
