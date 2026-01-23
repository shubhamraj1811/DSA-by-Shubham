"""
Day 50

🚀 217. Contains Duplicate

🤖 Question : Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
⚠️ Difficulty : 🟩Easy
🧩 Topics : Array, Hash Table, Sorting
🏢 Companies : 

🔮 Algorithm : Hash Set

1. Create an empty set.
2. Start a loop for n in nums.
3. Check if n is present in the set.
4. If it is present, return True.
5. If it is not, add n to the set.
6. If loop completes, return false.

💎 Time Complexity : O(n)
💎 Space Complexity : O(n)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False

# main code
if __name__ == "__main__":
    num1 = [7, 1, 5, 3, 6, 4]
    num2 = [1,1,1,3,3,4,3,2,4,2]

    sol = Solution()
    print("For num1 : ", sol.containsDuplicate(num1)) # False
    print("For num2 : ", sol.containsDuplicate(num2)) # True