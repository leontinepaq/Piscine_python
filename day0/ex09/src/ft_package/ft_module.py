def add_one(number):
    """
    Increment the given number by 1.

    Args:
        number: A numeric value (int or float).

    Returns:
        The value of number + 1.
    """
    return number + 1


def count_in_list(lst: list, el) -> int:
    """
    Count the number of occurrences of an element in a list.

    Args:
        lst (list): The list to search.
        el: The element to count.

    Returns:
        int: The number of times el appears in lst.
    """
    return lst.count(el)
