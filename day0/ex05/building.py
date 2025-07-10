"""
Takes a single string argument and displays the sums of its upper-case
characters, lower-case characters, punctuation characters, digits and spaces
"""

import sys


def is_punct(c):
    if c in ".,;\"'-?:!":
        return True
    return False


def count_chars(text: str) -> str:
    """
    Returns a string summarizing character counts by category

    Args:
        text (str): The input string to be processed

    Returns:
        The summary of character types
    """
    nb_chars = len(text)
    nb_upper = sum(c.isupper() for c in text)
    nb_lower = sum(c.islower() for c in text)
    nb_digits = sum(c.isdigit() for c in text)
    nb_space = sum(c.isspace() for c in text)
    nb_punct = sum(is_punct(c) for c in text)

    return (
        f"The text contains {nb_chars} characters:\n"
        f"{nb_upper} upper letters\n"
        f"{nb_lower} lower letters\n"
        f"{nb_punct} punctuation marks\n"
        f"{nb_space} spaces\n"
        f"{nb_digits} digits"
    )


def main():
    """
    Main function: handles argument parsing and error management.
    """

    args = sys.argv[1:]

    try:
        if not args:
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            assert len(args), "only one argument is expected"
            text = args[0]

        result = count_chars(text)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
