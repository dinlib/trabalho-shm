from enum import Enum


class FileType(Enum):
    TEXT = "txt"
    MORSE = "morse"
    AUDIO = "wav"


def read_file(filename):
    with open(filename) as file:
        content = file.read()
        file_extension = filename.split('.')[-1]

    return (content, FileType(file_extension))


def dump(text, audio, morse, filename):
    if text:
        dump_text(text, filename)

    if audio:
        dump_audio(audio, filename)

    if morse:
        dump_morse(morse, filename)


def dump_text(text, filename):
    output_path = '{}.{}'.format(filename, FileType.TEXT.value)
    with open(output_path, 'w') as file:
        file.write(text)


def dump_morse(morse, filename):
    output_path = '{}.{}'.format(filename, FileType.MORSE.value)
    with open(output_path, 'w') as file:
        file.write(morse)


def dump_audio(audio, filename):
    raise NotImplementedError
