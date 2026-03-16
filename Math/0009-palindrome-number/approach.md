# 💡 Approach For Palindrome Number
[View Solution](solution.py)  
[View Test File](testsolution.py)  


## 💡 Intuition

## What is a Palindrome Number?
A Number that reads the same forward and backwards.

**Examples:**  
Input: x = 121     → Output: true   ✅  (121 reversed = 121)  
Input: x = -121    → Output: false  ❌  (-121 reversed = 121- , not same)  
Input: x = 10      → Output: false  ❌  (10 reversed = 01 = 1, not same)  
Input: x = 0       → Output: true   ✅  (0 reversed = 0)  


## Key Observations before solving:
- All negative numbers are not palindrome. Becz of -ve sign.
- Numbers which ends with zero cannot be palindrome. 100 reads 001 backwards.
- Single digit numbers → Always palindrome.


------------------  


# All Possible Approach

## Method 1: String Conversion Method (Brute Force)
1. Convert the number to a string
2. Reverse the string
3. Check if it matches the original

**Examples:**  
`121  →  "121"  →  reverse = "121"  →  equal ✅`

- **Pros:** Very Simple to implement
- **Cons:** Uses extra space for the string, and many interviewers will explicitly forbid it to test your math logic.
- **Time Complexity:** O(n) where n = number of digits
- **Space Complexity:** O(d) — extra string created


## Method 2: Reverse Full Number

Reverse the entire integer mathematically and compare with original.  

**Examples:**  
`x = 121`  
`reversed = 121`  
`121 == 121 → true ✅`  

- **Pros:** Space Complexity is O(1)
- **Downside:** Risk of integer overflow when reversing large numbers.


## Method 3: Reverse Only Half the Number ⭐ OPTIMAL
We don't need to reverse the full number!
Just reverse the second half and compare it with the first half.

**Examples:**  
`x = 1221`  
`First half  = 12`  
`Second half reversed = 12`  
`12 == 12 → true ✅`  

`x = 121`  
`First half  = 12  (odd digits, so we divide differently)`  
`Second half reversed = 121/10 = 12 (ignore middle digit)`  
`12 == 12 → true ✅`  

- Time Complexity: O(d/2) → effectively O(log n)
- Space Complexity: O(1)
- No overflow risk ✅
- No string conversion ✅

### Deep Dive 🔍
Why reverse only half?
- Reversing the full number risks overflow
- We only need symmetry — left half must mirror right half
- We stop at the middle of the number

## ⚙️ Algorithm

1. **Step 01 : Handle Edge Cases**
   1. If x < 0 , return false
   2. If x is not 0 and x ends with 0 , return false
2. **Edge Cases Passed, Now return the second Half :**
   1. Take reversed = 0
   2. while x is greater than reversed
   3. extract the last digit -> digit = x % 10
   4. Add the last digit to the reversed -> reversed * 10 + digit
   5. Remove the last digit -> x = x/10
3. **Step 03: Compare both halves**
   1. If even digits: x == reversed, return true
   2. If odd digits: x == reversed/10, return true

## 🐞 Psuedocode

```
function isPalindrome(x):

    // Step 1: Handle edge cases
    if x < 0:
        return false
    if x != 0 AND x % 10 == 0:
        return false

    // Step 2: Reverse the second half
    reversedHalf = 0
    while x > reversedHalf:
        digit = x % 10          // extract last digit
        reversedHalf = reversedHalf * 10 + digit
        x = x / 10              // remove last digit (integer division)

    // Step 3: Compare
    if even digits: x == reversedHalf
    if odd digits:  x == reversedHalf / 10   (discard middle digit)

    return (x == reversedHalf) OR (x == reversedHalf / 10)
```

## 📊 Complexity
- **Time Complexity:** $O(O(d/2))$ → effectively O(log n)
- **Space Complexity:** $O(1)$

---

## 💡 Hints:

💡 Handle negatives and trailing zeros first.  
💡 The while loop runs while x > reversedHalf.  
💡 At the end, check BOTH even and odd length cases.  

---

## 🧠 Key Takeaways
- What did I learn from this problem?

- Why did I choose this specific data structure?
