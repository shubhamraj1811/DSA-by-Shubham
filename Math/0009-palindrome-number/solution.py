class Solution:
  def isPalindrome(self, x: int) -> bool:
    # Edge Case:
    # Negative numbers are not palindrome.
    # Numbers that end with 0 -> not palindrome (except 0).
    if x < 0 or (x % 10 == 0 and x != 0):
      return False
    
    reversed = 0
    # reverse the second half
    while x > reversed:
      digit = x % 10                      # get the last digit
      reversed = reversed * 10 + digit    # add the digit to the reversed number
      x //= 10                            # remove the last digit from x

    # If the length is odd, we need to remove the middle digit from reversed
    return x == reversed or x == reversed // 10