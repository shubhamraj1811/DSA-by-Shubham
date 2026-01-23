"""
🚀 9. Palindrome

🤖 Question : Given an integer x, return True if x is a Palindrome and False otherwise.
⚠️ Difficulty : 🟩Easy
🧩 Topics : Math
🏢 Companies : Amazon, Microsoft, Apple, Google, Meta

⏳ Approach 1 : Revert Half of the Number
We can also solve this problem by taking the string of the number and checking if it reads the same forwards and backwards but this will use extra space.
Instead, we can revert half of the number and compare it with the other half.

This is the best DSA apporach because it uses O(1) space and O(log(n)) time.
In this approach, we revert half of the number and compare the first half with the other half of the number.

🔮 Algorithm : Revert Half of the Number
1. Edge Case: 
- If x is negative (x < 0), it cannot be palindrome. Return False.
- If x ends with 0 (x % 10 == 0) but is not 0 itself, it cannot be palindrome. Return False.

2. Create a variable 'reversed = 0' to store the reversed digits.

3. Logic:
- while x is greater than reversed (x > reversed):
    - Take the last digit of x (x % 10).
    - Add it to the reversed variable after multiplying it by 10 (reversed = reversed*10 + lastDigit).
    - Remove the last digit from x (x //= 10).

4 Comparison:
- For even length, if x == reversed, return True.
- For odd length, if x == reversed // 10, return True.

💎 Time Complexity : O(log10(n))
💎 Space Complexity : O(1)
"""

# Python Code


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Edge cases
        if x<0 or (x%10==0 and x!=0):
            return False
        # Step 2: Initialize Variable
        reversed = 0

        # Step 3: Revert half of the number
        while x>reversed:
            lastDigit = x%10
            reversed = reversed*10 + lastDigit
            x //= 10

        # Step 4: Comparison
        return x==reversed or x==reversed//10
    
# main code
if __name__ == "__main__":
    num = int(input("Enter an Integer: "))
    sol = Solution()
    print(f"Is {num} a Palindrome? : {sol.isPalindrome(num)}")