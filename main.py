import argparse

from file_helpers import FileType, read_file, dump
from text import parse_text_to_audio
from morse import parse_morse_to_audio, parse_morse_to_text, parse_text_to_morse
# from audio import parse_audio_to_morse, parse_audio_to_text


def main():
    parser = argparse.ArgumentParser(
        description='Parse text, morse and audio files.')
    parser.add_argument('file_path', type=str, help='path for input file')
    args = parser.parse_args()

    file_path = args.file_path
    (content, file_type) = read_file(file_path)

    file_path_no_extension = file_path.split('.')[0]

    if file_type == FileType.TEXT:
        morse = parse_text_to_morse(content)
        # audio = parse_text_to_audio(content)
        dump(None, None, morse, file_path_no_extension)
    elif file_type == FileType.MORSE:
        text = parse_morse_to_text(content)
        audio = parse_morse_to_audio(content)
        dump(text, audio, None, file_path_no_extension)
    # else:
        # text = parse_audio_to_text(content)
        # morse = parse_audio_to_morse(content)
        # dump(text, None, morse, file_path_no_extension)


if __name__ == "__main__":
    main()
