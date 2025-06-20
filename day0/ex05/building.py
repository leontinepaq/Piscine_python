"""
Takes a single string argument and displays the sums of its upper-case
characters, lower-case characters, punctuation characters, digits and spaces
"""

import sys

def is_punct(c):
    if c in  ".,;\"'-?:!":
        return True
    return False

def count_chars(arg: str) -> str:
    """
    Returns a string summarizing character counts by category

    Args:
        arg (str): The input string to be processed

    Returns:
        The summary of character types
    """
    nb_chars = len(arg)
    nb_upper = sum(c.isupper() for c in arg)
    nb_lower = sum(c.islower() for c in arg)
    nb_digits = sum(c.isdigit() for c in arg)
    nb_space = sum(c.isspace() for c in arg)
    nb_punct = sum(is_punct(c) for c in arg)

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

    if not args:
        print("Please provide a string to process")
        return

    try:
        assert len(args) == 1, "only one argument is expected"
        result = count_chars(args[0])
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
