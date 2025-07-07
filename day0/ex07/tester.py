from sos import convert_to_morse, is_alphanum_or_space


def run_tests():
    test_cases = [
        # (input_string, expected_output)
        ("SOS", "... --- ..."),
        ("hello world", ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
        ("A B C", ".- / -... / -.-."),
        ("123", ".---- ..--- ...--"),
        ("", ""),
    ]

    all_passed = True
    for i, (input_str, expected) in enumerate(test_cases, 1):
        # Test validation function
        valid = is_alphanum_or_space(input_str)
        if not valid:
            print(f"❌ Test {i} failed validation check: {input_str!r} "
                  "should be valid")
            all_passed = False
            continue

        # Test conversion
        result = convert_to_morse(input_str)
        if result != expected:
            print(f"❌ Test {i} failed:")
            print(f"   Input: {input_str!r}")
            print(f"   Expected: {expected!r}")
            print(f"   Got     : {result!r}\n")
            all_passed = False
        else:
            print(f"✅ Test {i} passed.")

    # Test invalid inputs for validation function
    invalid_inputs = ["hello!", "hi$", "test@", "éà", "newline\n"]
    for invalid in invalid_inputs:
        if is_alphanum_or_space(invalid):
            print(f"❌ Validation failed: {invalid!r} should be invalid")
            all_passed = False
        else:
            print(f"✅ Validation test passed for invalid input: {invalid!r}")

    if all_passed:
        print("\n🎉 All tests passed!")


if __name__ == "__main__":
    run_tests()
