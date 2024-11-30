# `morse-code`

**Usage**:

```console
$ morse-code [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `encrypt`: Encrypts the given text or file content to...
* `decrypt`: Decrypts the given Morse code or file...

## `morse-code encrypt`

Encrypts the given text or file content to Morse code.

**Usage**:

```console
$ morse-code encrypt [OPTIONS] [TEXT]
```

**Arguments**:

* `[TEXT]`: Text to be encrypted to morse code

**Options**:

* `-i, --input TEXT`: Specify the input file
* `-o, --output TEXT`: Specify the output file
* `--help`: Show this message and exit.

## `morse-code decrypt`

Decrypts the given Morse code or file content to text.

**Usage**:

```console
$ morse-code decrypt [OPTIONS] [MORSE_CODE]
```

**Arguments**:

* `[MORSE_CODE]`: Morse code to be decrypted to clear text

**Options**:

* `-i, --input TEXT`: Specify the input file
* `-o, --output TEXT`: Specify the output file
* `--help`: Show this message and exit.
