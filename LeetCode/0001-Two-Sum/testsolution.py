from solution import Solution

def run_tests():
    sol = Solution()
    
    # Define the criteria: (input_list, target, expected_output, name)
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1], "Test Case 1"),
        ([3, 2, 4], 6, [1, 2], "Test Case 2"),
        ([3, 3], 6, [0, 1], "Test Case 3"),
    ]

    for nums, target, expected, name in test_cases:
        actual = sol.twoSum(nums, target)
        
        # Criteria check: compare the actual result to the expected result
        # Note: We sort them just in case the indices come back in a different order
        is_passed = sorted(actual) == sorted(expected)
        
        status = "✅ Passed" if is_passed else f"❌Failed (Expected {expected}, got {actual})"
        
        print(f"{name}")
        print(f"Status: {status}")
        print("-" * 20)

if __name__ == '__main__':
    run_tests()