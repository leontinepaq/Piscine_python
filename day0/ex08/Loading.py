def format_progress_bar(idx, len_lst) -> str:
    """
    Format the progress bar string for a given index in an iterable.

    Parameters:
    - idx (int): The current index in the iteration.
    - len_lst (int): The total number of elements in the iterable.

    Returns:
    - str: A formatted string representing the progress bar,
           including the percentage, a bar of width 50, and the counter.
    """

    percent = idx / len_lst
    bar_width = 50
    bar = "█" * int(percent * bar_width)
    return f"{percent:>4.0%}|{bar:<{bar_width}}| {idx}/{len_lst}"


def ft_tqdm(lst: range) -> None:
    """
    A simplified version of tqdm that displays a progress bar
    in the terminal for an iterable (only range supported).

    Parameters:
    - lst (range): A Python range object to iterate over.

    Yields:
    - int: The current value in the iteration, just like a regular for-loop.
    """
    len_lst = len(lst)

    for i, value in enumerate(lst):
        print(format_progress_bar(i, len_lst), end="\r")
        yield value

    print(format_progress_bar(len_lst, len_lst))
