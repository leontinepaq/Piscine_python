def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return (
        [x for x in iterable if function(x)]
        if function
        else [x for x in iterable if x]
    )


# def test_ft_filter():
#     test_cases = [
#         (lambda x: x % 2 == 0, [1, 2, 3, 4, 5]),
#         (str.isupper, ["a", "B", "C", "d"]),
#         (None, [0, 1, False, True, "", "hello", []]),
#         (lambda x: x > 3, range(10)),
#         (None, ""),
#     ]

#     for i, (func, iterable) in enumerate(test_cases, 1):
#         expected = list(filter(func, iterable))
#         result = list(ft_filter(func, iterable))
#         assert result == expected, f"Test {i} failed:\
# 			\nExpected: {expected}\nGot: {result}"

#     print("✅ All tests passed!")


# if __name__ == "__main__":
#     test_ft_filter()
