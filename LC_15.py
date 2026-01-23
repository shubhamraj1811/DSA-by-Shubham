"""
⏳ Day 53

🚀 15. 3 Sum

🤖 Question : Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
⚠️ Difficulty : 🟨 Medium
🧩 Topics : Array, Two Pointer, Sorting
🏢 Companies : Amazon, Microsoft, Apple, Google, Meta, Adobe

🔮 Algorithm : Sort + Two Pointer

1. Sort the array. It allow us to skip duplicates and use two pointer.
2. Loop the array with i : from 0 to n-2 , i is the first num in the triplet.
3. If the current number nums[i] is the same as the one before it (nums[i-1]), we skip it and continue to the next iteration. This prevents us from finding duplicate triplets starting with the same number.
4. For each i, we initialize two more pointers: l (left pointer) starts at i + 1 and r (right pointer) starts at the end of the array, len(nums) - 1.
5. Now we move l and r towards each other (while l < r) to find the other two numbers that, with nums[i], sum to zero.
Case 1 :: Current_sum < 0 [ The sum is too small. We need a larger number. ] :: Move the left pointer to the right: l += 1.
Case 2 :: Current_sum > 0 [ The sum is too large. We need a smaller number. ] :: Move the right pointer to the left: r -= 1.
Case 3 :: Current_sum == 0 [ Success! We found a valid triplet: [nums[i], nums[l], nums[r]].] :: Add this triplet to our result list.
6. After finding triplets avoid duplicates :
|a| Increment l (l += 1).
|b| while nums[l] == nums[l-1] and l < r: l += 1. This skips all duplicates for the left pointer.
7. After the main loop finishes, return the list of found triplets.

💎 Time Complexity : O(n^2)
💎 Space Complexity : O(n)
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array

        # Step 2: Iterate with the 'i' pointer
        for i in range(len(nums) - 2):
            
            # Step 3: Skip duplicates for 'i'
            # (Check if i > 0 to avoid index out of bounds)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 4: Set up two pointers
            l, r = i+1, len(nums)-1

            # Step 5: Two-pointer search
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum < 0:     # Case 1: Sum is too small
                    l += 1
                elif sum > 0:   # Case 2: Sum is too large
                    r -= 1
                else:           # Case 3: Found a triplet!
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # Step 6: Skip duplicates for 'l' and 'r'
                    l += 1
                    r -= 1
                    # Skip duplicates on both sides
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res # Step 7: Return the result
    
# main code
if __name__ == "__main__":
    num1 = [-1,0,1,2,-1,-4]

    sol = Solution()
    print("For num1 : ", sol.threeSum(num1))