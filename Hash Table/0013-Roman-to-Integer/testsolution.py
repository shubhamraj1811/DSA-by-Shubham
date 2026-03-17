from solution import Solution

def run_tests():
    sol = Solution()

    # (input_data, expected_output)
    test_cases = [
        ((), ()),
        ((), ()),
    ]
    
    for i, (data, expected) in enumerate(test_cases):
        # result = sol.solve(data)
        # print(f"Test Case {i+1}: {'✅ Pass' if result == expected else '❌ Fail'}")
        print(f"Test Case {i+1} initialized.")

if __name__ == '__main__':
    run_tests()