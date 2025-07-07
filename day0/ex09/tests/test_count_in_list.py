from ft_package import count_in_list


def run_tests():
    test_cases = [
        (["toto", "tata", "toto"], "toto", 2),
        (["toto", "tata", "toto"], "tutu", 0),
        ([1, 2, 3, 2, 2], 2, 3),
        (["a", "b", "a", "c"], "a", 2),
        ([], 42, 0),
        ([None, None, 1], None, 2),
        ([True, False, True], True, 2),
    ]

    all_passed = True

    for i, (lst, el, expected) in enumerate(test_cases, 1):
        result = count_in_list(lst, el)
        passed = result == expected
        status = "✅ Success" if passed else "❌ Failure !"
        print(
            f"Test {i}:\ncount_in_list({lst!r}, {el!r}) = {result}, expected {expected}\n{status}\n"
        )
        if not passed:
            all_passed = False

    if all_passed:
        print("\n🎉 All tests passed!")


if __name__ == "__main__":
    run_tests()
