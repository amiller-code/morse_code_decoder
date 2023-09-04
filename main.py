# Morse Code Translator
# 2023-07-15
# DegaBoo

MORSE_DICTIONARY = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/"
}


def translator():
    # set variable to allow for repeat translations
    keep_translating = 'y'

    while keep_translating == 'y':
        # ask for a word or phrase from the user
        starting = input('Type in a word or phrase to get started! (Only english alphabet characters, numbers, or '
                         'the following punctuation: .,?!-/@()\n')

        # lower all characters to allow for comprehension in the dictionary keys
        no_space_starting = starting.lower()

        # check whether all characters are in the dictionary above
        # throw an error and restart if there are invalid characters
        if False in (char in MORSE_DICTIONARY.keys() for char in no_space_starting):
            print('Error: please only use the characters from the given options\n')
            continue

        translated = ''
        # start looping through the characters, translate, and append that to the translated variable
        for char in no_space_starting:
            translated += MORSE_DICTIONARY[char] + ' '

        # print the translated word and ask if they'd like to try another
        print(f'To say {starting} in Morse Code, type\n{translated}')
        keep_translating = input('\nWould you like to translate more? (Y/N): ').lower()
        # if they don't type in y or n, ask again until they do
        while keep_translating not in ['y', 'n']:
            keep_translating = input('Would you like to translate more? (Y/N): ').lower()

    # sendoff after exiting while loop
    print('Have a good day!')


if __name__ == '__main__':
    translator()
