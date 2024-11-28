from typing import Optional
import converter
import typer
from typing_extensions import Annotated


app = typer.Typer(rich_markup_mode="rich")

converter = converter.Converter()


@app.command()
def convert(morse: Annotated[bool, typer.Option("--morse", "-m", help="Convert morse to plain text")] = False):
    if morse:
        morse_code = typer.prompt("Type the morse code to be converted to clear text")
        message = converter.decrypt_message(morse_code)
    else:
        text = typer.prompt("Type the message to be converted to morse code")
        message = converter.encrypt_message(text)

    print(f"The message: {message}")




if __name__ == "__main__":
    app()