"""
This script takes two arguments: a string `s` and an integer `n`.
It prints a list of words from `s` that are strictly longer than `n`.
Words are split by spaces.

Usage examples:
$ python filterstring.py 'Hello the World' 4
['Hello', 'World']

$ python filterstring.py
AssertionError: the arguments are bad
"""

import sys
from ft_filter import ft_filter

# def clean_to_alnum(s: str)-> str:
#     """
#     Removes all non-alphanumeric characters from a string
#     Args:
#         s (str): The input string

#     Returns:
#         str: A new string containing only alphanumeric characters
#     """
#     return ''.join(ft_filter(str.isalnum, s))


def filter_long_words(s: str, n: int) -> list:
    """
    Returns a list of cleaned words from s that are longer than n

    Args:
        S (str): The input string
        N (int): The minimum word lenght to include

    Returns:
        list: The list of cleaned words longer than n
    """
    words = s.split()
    return ft_filter(lambda word: len(word) > n, words)


def main():
    """
    Main function: parses arguments and prints long words from input string
    """
    args = sys.argv[1:]

    try:
        if len(args) != 2:
            raise AssertionError("the arguments are bad")

        try:
            num = int(args[1])
        except ValueError:
            raise AssertionError("the arguments are bad")

        result = filter_long_words(args[0], num)
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    main()
