from enum import Enum


class FileType(Enum):
    TEXT = "txt"
    MORSE = "morse"
    AUDIO = "wav"


DOT = '1'
TRACE = '111'
SPACE_LETTER = '0'
SPACE_BETWEEN_LETTERS = '000'
SPACE_BETWEEN_WORDS = '0000000'


MORSE_TABLE = {
    'A': [DOT, TRACE],
    'B': [TRACE, DOT, DOT, DOT],
    'C': [TRACE, DOT, TRACE, DOT],
    'D': [TRACE, DOT, DOT],
    'E': [DOT],
    'F': [DOT, DOT, TRACE, DOT],
    'G': [TRACE, TRACE, DOT],
    'H': [DOT, DOT, DOT, DOT],
    'I': [DOT, DOT],
    'J': [DOT, TRACE, TRACE, TRACE],
    'K': [TRACE, DOT, TRACE],
    'L': [DOT, TRACE, DOT, DOT],
    'M': [TRACE, TRACE],
    'N': [TRACE, DOT],
    'O': [TRACE, TRACE, TRACE],
    'P': [DOT, TRACE, TRACE, DOT],
    'Q': [TRACE, TRACE, DOT, TRACE],
    'R': [DOT, TRACE, DOT],
    'S': [DOT, DOT, DOT],
    'T': [TRACE],
    'U': [DOT, DOT, TRACE],
    'V': [DOT, DOT, DOT, TRACE],
    'W': [DOT, TRACE, TRACE],
    'X': [TRACE, DOT, DOT, TRACE],
    'Y': [TRACE, DOT, TRACE, TRACE],
    'Z': [TRACE, TRACE, DOT, DOT],
    '1': [DOT, TRACE, TRACE, TRACE, TRACE],
    '2': [DOT, DOT, TRACE, TRACE, TRACE],
    '3': [DOT, DOT, DOT, TRACE, TRACE],
    '4': [DOT, DOT, DOT, DOT, TRACE],
    '5': [DOT, DOT, DOT, DOT, DOT],
    '6': [TRACE, DOT, DOT, DOT, DOT],
    '7': [TRACE, TRACE, DOT, DOT, DOT],
    '8': [TRACE, TRACE, TRACE, DOT, DOT],
    '9': [TRACE, TRACE, TRACE, TRACE, DOT],
    '0': [TRACE, TRACE, TRACE, TRACE, TRACE],
}

SUPPORTED_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def read_file(filename):
    with open(filename) as file:
        content = file.read()
        file_extension = filename.split('.')[-1]

    return (content, FileType(file_extension))


def parse_text_to_morse(text):
    upper_text = text.upper()
    words = upper_text.split(' ')
    clean_words = map(lambda word: filter(
        lambda c: c in SUPPORTED_CHARS, word), words)
    return SPACE_BETWEEN_WORDS.join(
        map(lambda word: SPACE_BETWEEN_LETTERS.join(map(lambda l: SPACE_LETTER.join(MORSE_TABLE[l]), word)), clean_words))


def main():
    (content, file_extension) = read_file('teste.txt')
    print(parse_text_to_morse(content))


if __name__ == "__main__":
    main()
