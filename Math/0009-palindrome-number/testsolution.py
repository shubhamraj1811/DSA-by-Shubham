from solution import Solution

def run_tests():
  sol = Solution()
  # (input, expected_output, name)
  test_cases = [
    (121, True, "Test Case 1"),
    (-121, False, "Test Case 2"),
    (10, False, "Test Case 3"),
    (0, True, "Test Case 4"),
    (12321, True, "Test Case 5"),
    (123, False, "Test Case 6"),
    (11, True, "Test Case 7"),
    (8, True, "Test Case 8"),
    (1001, True, "Test Case 9"),
    (123456789, False, "Test Case 10")
  ]

  for x, expected, name in test_cases:
    result = sol.isPalindrome(x)
    status = "✅ Passed" if result == expected else f"❌ Failed (Expected {expected}, got {result})"
    print(f"{name}: Input: {x} | Expected: {expected} | Result: {result} | Status: {status}")

if __name__ == '__main__':
  run_tests()