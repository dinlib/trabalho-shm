import audio.signalwave as signalwave
import numpy as np

DOT = '1'
DASH = '111'
SPACE_LETTER = '0'
SPACE_BETWEEN_LETTERS = '000'
SPACE_BETWEEN_WORDS = '0000000'

SUPPORTED_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

MORSE_TO_TEXT_TABLE = {
    DOT + SPACE_LETTER + DASH: 'A',
    DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT: 'B',
    DASH + SPACE_LETTER + DOT + SPACE_LETTER + DASH + SPACE_LETTER + DOT: 'C',
    DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT: 'D',
    DOT: 'E',
    DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH + SPACE_LETTER + DOT: 'F',
    DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT: 'G',
    DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT: 'H',
    DOT + SPACE_LETTER + DOT: 'I',
    DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH: 'J',
    DASH + SPACE_LETTER + DOT + SPACE_LETTER + DASH: 'K',
    DOT + SPACE_LETTER + DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT: 'L',
    DASH + SPACE_LETTER + DASH: 'M',
    DASH + SPACE_LETTER + DOT: 'N',
    DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH: 'O',
    DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT: 'P',
    DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT + SPACE_LETTER + DASH: 'Q',
    DOT + SPACE_LETTER + DASH + SPACE_LETTER + DOT: 'R',
    DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT: 'S',
    DASH: 'T',
    DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH: 'U',
    DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH: 'V',
    DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH: 'W',
    DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH: 'X',
    DASH + SPACE_LETTER + DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH: 'Y',
    DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT: 'Z',
    DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH: '1',
    DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH: '2',
    DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH: '3',
    DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH: '4',
    DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT: '5',
    DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT: '6',
    DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT: '7',
    DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT: '8',
    DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT: '9',
    DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH: '0',
}

TEXT_TO_MORSE_TABLE = {
    'A': DOT + SPACE_LETTER + DASH,
    'B': DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT,
    'C': DASH + SPACE_LETTER + DOT + SPACE_LETTER + DASH + SPACE_LETTER + DOT,
    'D': DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT,
    'E': DOT,
    'F': DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH + SPACE_LETTER + DOT,
    'G': DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT,
    'H': DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT,
    'I': DOT + SPACE_LETTER + DOT,
    'J': DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH,
    'K': DASH + SPACE_LETTER + DOT + SPACE_LETTER + DASH,
    'L': DOT + SPACE_LETTER + DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT,
    'M': DASH + SPACE_LETTER + DASH,
    'N': DASH + SPACE_LETTER + DOT,
    'O': DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH,
    'P': DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT,
    'Q': DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT + SPACE_LETTER + DASH,
    'R': DOT + SPACE_LETTER + DASH + SPACE_LETTER + DOT,
    'S': DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT,
    'T': DASH,
    'U': DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH,
    'V': DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH,
    'W': DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH,
    'X': DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH,
    'Y': DASH + SPACE_LETTER + DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH,
    'Z': DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT,
    '1': DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH,
    '2': DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH,
    '3': DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH + SPACE_LETTER + DASH,
    '4': DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DASH,
    '5': DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT,
    '6': DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT,
    '7': DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT + SPACE_LETTER + DOT,
    '8': DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT + SPACE_LETTER + DOT,
    '9': DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DOT,
    '0': DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH + SPACE_LETTER + DASH,
}

#####################
### MORSE -> TEXT ###
#####################


def parse_morse_to_text(morse):
    words = morse.split(SPACE_BETWEEN_WORDS)
    words_in_text = map(transform_word_to_text, words)
    return ' '.join(words_in_text)


def transform_word_to_text(word):
    letters = word.split(SPACE_BETWEEN_LETTERS)
    return ''.join(map(transform_letter_to_text, letters))


def transform_letter_to_text(letter):
    return MORSE_TO_TEXT_TABLE[letter]


#####################
### TEXT -> MORSE ###
#####################

def parse_text_to_morse(text):
    words = text.upper().split(' ')
    clean_words = map(filter_only_supported_chars, words)
    words_in_morse = map(transform_word_to_morse, clean_words)
    return SPACE_BETWEEN_WORDS.join(words_in_morse)


def filter_only_supported_chars(word):
    return filter(lambda c: c in SUPPORTED_CHARS, word)


def transform_word_to_morse(word):
    return SPACE_BETWEEN_LETTERS.join(map(transform_letter_to_morse, word))


def transform_letter_to_morse(letter):
    return TEXT_TO_MORSE_TABLE[letter]


def parse_morse_to_audio(morse):
    frequency = 440
    sampling_rate = 48000
    amplitude = 16000
    time_ = 3

    waves = np.array([])

    words = morse.split(SPACE_BETWEEN_WORDS)
    for word in words:
        letters = word.split(SPACE_BETWEEN_LETTERS)
        for letter in letters:
            components = letter.split(SPACE_LETTER)
            for component in components:
                time_ = 0.25 if component == DOT else 0.75
                wave = signalwave.signalwave(
                    frequency, sampling_rate, time=time_)
                waves = np.concatenate((waves, np.array(wave)))
                wave = signalwave.signalwave(0, sampling_rate, time=0.25)
                waves = np.concatenate((waves, np.array(wave)))

            wave = signalwave.signalwave(0, sampling_rate, time=0.75)
            waves = np.concatenate((waves, np.array(wave)))

        wave = signalwave.signalwave(0, sampling_rate, time=0.25 * 7)
        waves = np.concatenate((waves, np.array(wave)))

    return waves
