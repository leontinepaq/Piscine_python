def format_progress_bar(idx, len_lst) -> str:
    percent = idx / len_lst
    bar_width = 50
    bar = '█' * int(percent * bar_width)
    return f"{percent:>4.0%}|{bar:<{bar_width}}| {idx}/{len_lst}"

def ft_tqdm(lst: range) -> None:
    len_lst = len(lst)

    for i, value in enumerate(lst) :
        print(format_progress_bar(i, len_lst), end = '\r')
        yield value

    print(format_progress_bar(len_lst, len_lst))

