from typer.testing import CliRunner

from src.cli.main import app

TEXT_FILE = "text.txt"

TEST_DIR = "test"

ENCRYPT = "encrypt"
DECRYPT = "decrypt"
SOS = "sos"
SOS_MORSE_CODE = "... --- ..."
HELP_SOS = "help sos"
HELP_SOS_MORSE_CODE = ".... . .-.. .--.  ... --- ..."

runner = CliRunner()

def test_encrypt_text_without_spaces():
    result = runner.invoke(app, [ENCRYPT, SOS])
    assert result.exit_code == 0
    assert SOS_MORSE_CODE in result.stdout

def test_decrypt_morse_without_spaces():
    result = runner.invoke(app, [DECRYPT, SOS_MORSE_CODE])
    assert result.exit_code == 0
    assert SOS in result.stdout

def test_encrypt_text_with_spaces():
    result = runner.invoke(app, [ENCRYPT, HELP_SOS])
    assert result.exit_code == 0
    assert HELP_SOS_MORSE_CODE in result.stdout

def test_decrypt_morse_with_spaces():
    result = runner.invoke(app, [DECRYPT, HELP_SOS_MORSE_CODE])
    assert result.exit_code == 0
    assert HELP_SOS in result.stdout

def test_encrypt_input_file_without_spaces(tmp_path):
    directory = tmp_path / TEST_DIR
    directory.mkdir()
    path = directory / TEXT_FILE
    path.write_text(SOS, encoding="utf-8")

    result = runner.invoke(app, [ENCRYPT, "-i", path])
    assert result.exit_code == 0
    assert SOS_MORSE_CODE in result.stdout

def test_encrypt_input_file_with_spaces(tmp_path):
    directory = tmp_path / TEST_DIR
    directory.mkdir()
    path = directory / TEXT_FILE
    path.write_text(HELP_SOS, encoding="utf-8")

    result = runner.invoke(app, [ENCRYPT, "-i", path])
    assert result.exit_code == 0
    assert HELP_SOS_MORSE_CODE in result.stdout


def test_decrypt_input_file_with_spaces_to_output_file(tmp_path):
    directory = tmp_path / TEST_DIR
    directory.mkdir()
    path = directory / TEXT_FILE
    output_path = directory / "out.txt"
    path.write_text(HELP_SOS_MORSE_CODE, encoding="utf-8")

    result = runner.invoke(app, [DECRYPT, "-i", path, "-o", output_path])
    assert result.exit_code == 0
    assert output_path.read_text(encoding="utf-8") == HELP_SOS
