from file_helpers import FileType, read_file, dump
from text import parse_text_to_morse, parse_text_to_audio
from morse import parse_morse_to_audio, parse_morse_to_text
from audio import parse_audio_to_morse, parse_audio_to_text


def main():
    file_path = '/Users/guilherme/Sources/trabalho-shm/teste.txt'
    (content, file_type) = read_file(file_path)

    filename = file_path.split('.')[0]

    if file_type == FileType.TEXT:
        morse = parse_text_to_morse(content)
        # audio = parse_text_to_audio(content)
        dump(None, None, morse, filename)
    elif file_type == FileType.MORSE:
        text = parse_morse_to_text(content)
        audio = parse_morse_to_audio(content)
        dump(text, audio, None, filename)
    else:
        text = parse_audio_to_text(content)
        morse = parse_audio_to_morse(content)
        dump(text, None, audio, filename)


if __name__ == "__main__":
    main()
