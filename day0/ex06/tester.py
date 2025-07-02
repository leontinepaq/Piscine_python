from filterstring import (
    filter_long_words,
)  # remplace `your_module` par le nom de ton fichier sans `.py`


def run_tests():
    test_cases = [
        # (input_string, min_length, expected_result)
        ("Hello world", 3, ["Hello", "world"]),
        ("This is a test", 2, ["This", "test"]),
        ("42 is a number", 1, ["42", "is", "number"]),
        ("Short words only  a I an on", 2, ["Short", "words", "only"]),
        ("", 1, []),
    ]

    all_passed = True
    for i, (input_str, n, expected) in enumerate(test_cases, 1):
        result = filter_long_words(input_str, n)
        if result != expected:
            print(f"❌ Test {i} failed:")
            print(f"   Input: {input_str!r}, n={n}")
            print(f"   Expected: {expected}")
            print(f"   Got     : {result}\n")
            all_passed = False
        else:
            print(f"✅ Test {i} passed.")

    if all_passed:
        print("\n🎉 All tests passed!")


if __name__ == "__main__":
    run_tests()
