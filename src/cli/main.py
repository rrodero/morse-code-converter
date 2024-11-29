from typing import Optional
import typer
from typing_extensions import Annotated

from src.cli.converter import Converter

app = typer.Typer(rich_markup_mode="rich", no_args_is_help=True)

converter = Converter()

@app.command()
def encrypt(text: Annotated[Optional[str], typer.Argument(help="Text to be encrypted to morse code")] = None,
            input_file: Annotated[str, typer.Option("--input", "-i", help="Specify the input file")] = None,
            output_file: Annotated[str, typer.Option("--output", "-o", help="Specify the output file")] = None):

    morse_code = ""
    if text:
        morse_code = converter.encrypt_message(text)
    elif input_file:
        try:
            with open(input_file, "r") as input_file:
                for line in input_file:
                    morse_code += converter.encrypt_message(line)
        except FileNotFoundError:
            print("Input file was not found")
            raise typer.Exit(code=1)
    else:
        print("No provided message or input file to encrypt")
        raise typer.Abort()

    if output_file:
        try:
            with open(output_file, "w") as output_file:
                output_file.write(morse_code)
        except FileNotFoundError:
            print("Output file was not found")
            raise typer.Exit(code=1)
    else:
        print(morse_code)



@app.command()
def decrypt(morse_code: Annotated[Optional[str], typer.Argument()] = None,
            input_file: Annotated[str, typer.Option("--input", "-i", help="Specify the input file")] = None,
            output_file: Annotated[str, typer.Option("--output", "-o", help="Specify the output file")] = None):

    text = ""
    if morse_code:
        text = converter.decrypt_message(morse_code)
    elif input_file:
        try:
            with open(input_file, "r") as input_file:
                for line in input_file:
                    text += converter.decrypt_message(line)
        except FileNotFoundError:
            print("Input file was not found")
            raise typer.Exit(code=1)
    else:
        print("No provided morse code or input file to decrypt")
        raise typer.Abort()

    if output_file:
        try:
            with open(output_file, "w") as output_file:
                output_file.write(text)
        except FileNotFoundError:
            print("Output file was not found")
            raise typer.Exit(code=1)
    else:
        print(text)




if __name__ == "__main__":
    app()