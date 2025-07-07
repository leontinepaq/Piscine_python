from ft_package import add_one


def run_tests():
    test_cases = [
        (0, 1),
        (1, 2),
        (-1, 0),
        (100, 101),
        (-100, -99),
    ]

    all_passed = True
    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = add_one(input_val)
        print(f"Test {i}: add_one({input_val}) = {result}, expected {expected}")
        if result != expected:
            print("❌ Failure !\n")
            all_passed = False
        else:
            print("✅ Success\n")

    if all_passed:
        print("\n🎉 All tests passed!")

if __name__ == "__main__":
    run_tests()
