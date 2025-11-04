"""
⏳ Day 54 - 2 oct
🚀 18. 4Sum

🤖 Question : Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
⚠️ Difficulty : 🟨 Medium
🧩 Topics : Array, Two Pointer, Sorting
🏢 Companies : Amazon, Microsoft, Apple, Google, Meta, Adobe

🔮 Algorithm : Sort + Two Pointer

1. Sort the array. Let us use two pointer and skip duplicates. And start an empty set.

2. Outer Loop :
[a]. Start with i. This i will be the first number.
[b]. Base check : check if i > 0 and nums[i] == nums[i-1], then continue.
[c]. This will help skip all duplicates.

3. Inner Loop :
[a]. Start with j = i+1. j is the second number in the quadruplets.
[b]. Skip Dupliates : If j > i+1 and nums[j] == nums[j-1], then continue.

4. Now we have two numbers and we need to find two more numbers with two pointers.
5. Two-Pointer : l = j+1 and r = len-1.

6. Start a loop : while l<r
[a]. Calc sum = i+j+l+r (nums)
[b]. Case 1 : if sum < target, move l pointer, l++
[c]. Case 2 : if sum > target, move r pointer, r--
[d]. Case 3 : if equal, add the result to list.

7. Skip Duplicates for l
[a]. Do l+1, while l<r and nums[l] == nums[l-1] : then increment l

8. Skip Duplicates for r
[a]. Do r-1, while l<r and nums[r] == nums[r+1] : then decrement r

9. After all loop finishes, return the result list.

💎 Time Complexity : O(n^3)
💎 Space Complexity : O(n)
"""

from typing import List

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        n = len(nums)
        
        # Step 1: Sort the array
        nums.sort()

        # Step 2: Outer loop for 'i' (first number)
        for i in range(n - 3):
            # Step 3: Skip duplicates for 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # --- This is now a 3Sum problem for target - nums[i] ---
            
            # Step 4: Second loop for 'j' (second number)
            for j in range(i + 1, n - 2):
                # Step 5: Skip duplicates for 'j'
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # --- This is now a 2Sum problem ---
                
                # Step 7: Set up two pointers
                l, r = j + 1, n - 1
                
                # Step 8: Two-pointer search
                while l < r:
                    current_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if current_sum < target:
                        # Case 1: Sum too small
                        l += 1
                    elif current_sum > target:
                        # Case 2: Sum too large
                        r -= 1
                    else:
                        # Case 3: Found a quadruplet!
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        
                        # Skip duplicates for 'l' and 'r'
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        
        return res # Step 9: Return result
    
# main code
if __name__ == "__main__":
    num1 = [1,0,-1,0,-2,2]
    target1 = 0

    sol = Solution()
    print("For num1 : ", sol.fourSum(num1, target1))