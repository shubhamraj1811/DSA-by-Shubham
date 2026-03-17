from solution import Solution

def run_tests():
    sol = Solution()
    # (input, expected_output, name)

    print("🚀 Running Test Cases for Leetcode 13: Roman to Integer →\n")

    test_cases = [
        ("III", 3, "Test Case 1"),
        ("IV", 4, "Test Case 2"),
        ("IX", 9, "Test Case 3"),
        ("LVIII", 58, "Test Case 4"),
        ("MCMXCIV", 1994, "Test Case 5"),
        ("MMXXIV", 2024, "Test Case 6"),
        ("CDXLIV", 444, "Test Case 7"),
        ("CMXCIX", 999, "Test Case 8"),
        ("DCCCXC", 890, "Test Case 9"),
        ("MMMCMXCIX", 3999, "Test Case 10")
    ]

    for i, (data, expected, name) in enumerate(test_cases):
        result = sol.romanToInt(data)
        print(f"Test Case {i+1} ({name}): {'✅ Pass' if result == expected else '❌ Fail'}")

if __name__ == '__main__':
    run_tests()
