"""
Converts a string into Morse Code
"""

import sys

MORSE_CODE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def is_alphanum_or_space(s: str) -> bool:
    """Return True if all chars are ASCII alpha-numeric or space"""
    return all((c.isalnum() or c == " ") and ord(c) < 128 for c in s)
    # ord to exclude accents


def convert_to_morse(s: str) -> str:
    """
    Convert a string to Morse code

    Args:
        s (str): String with only alpha-numeric ASCII chars and spaces

    Returns:
        str: New string in Morse, letters separated by spaces,
        spaces replaced by "/"
    """
    return " ".join(MORSE_CODE[c.upper()] for c in s)


def main():
    """
    Main function: handles argument parsing and error management
    """
    args = sys.argv[1:]

    try:
        if len(args) != 1 or not is_alphanum_or_space(args[0]):
            raise SystemExit("AssertionError: the arguments are bad")
            # autre maniere de gerer erreurs
            # moins idiomatique que print + sys.exit(1)

        result = convert_to_morse(args[0])
        print(result)

    except Exception as e:
        sys.exit(f"Unexpected error: {e}")
        # appelle un SystemExit, idem moins idiomatique


if __name__ == "__main__":
    main()
