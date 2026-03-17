# 1️⃣ PROBLEM EXPLANATION

## What is the problem asking?
> Given a Roman numeral string s, convert it to an integer.

### The Roman Number System
```
| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |  
```

## The Subtraction Rule ⚠️ (The Tricky Part!)
* Normally, Roman numerals are added left to right.
* But when a smaller value appears BEFORE a larger value → it gets subtracted!

## The 6 Subtraction Cases
```
| Roman | Meaning  | Value |
|-------|----------|-------|
| IV    | 5-1      | 4     |
| IX    | 10-1     | 9     |
| XL    | 50-10    | 40    |
| XC    | 100-10   | 90    |
| CD    | 500-100  | 400   |
| CM    | 1000-100 | 900   |
```

### Example:

```
Input: s = "III"    → 1+1+1         = 3
Input: s = "LVIII"  → 50+5+1+1+1   = 58
Input: s = "MCMXCIV"→ 1000+900+90+4 = 1994
       M  CM  XC  IV
       ↑  ↑   ↑   ↑
      add sub sub sub
```


# 2️⃣ ALL POSSIBLE APPROACHES


## Method 1: Handle all Subtraction Cases Manually (Brute Force)

### Steps: 
1. Scan the String Character by Character
2. Manually check if current two characters form one of the 6 special pairs (IV, IX, XL...)
3. If yes → add that special value and skip 2 characters
4. If no → add single character value and move 1 step

```
TC → O(n)
SC → O(1)
```


## Method 2: Left to Right with Peek Ahead

### Steps:
1. Build a hashmap of symbol → value
2. Traverse left to right
3. At each character, peek at the next character
4. If current value < next value → subtract current
5. Else → add current

```
TC → O(n)
SC → O(1)  — hashmap is fixed 7 entries
```


## Method 3: Right to Left Traversal ⭐ OPTIMAL

### Steps: 
1. Build a hashmap of symbol → value
2. Traverse the String Right to Left
3. Compare current value with the previous ( which is to the right )
4. If current < previous → subtract current
5. Else → add current
6. Update previous at each step

### 📊 Complexity
```
TC → O(n)
SC → O(1)  — fixed size hashmap
```

✅ No peeking needed, no index out of bounds risk, cleanest logic

### Example:

**Walkthrough with "MCMXCIV" (= 1994):**

```
String:   M  C  M  X  C  I  V
Index:    0  1  2  3  4  5  6

Traverse RIGHT TO LEFT:

Step 1 → ch = V → curr=5      prev=0     5    > 0      → ADD 5     → total = 5     prev=5
Step 2 → ch = I → curr=1      prev=5     1    < 5      → SUB 1     → total = 4     prev=1
Step 3 → ch = C → curr=100    prev=1     100  > 1      → ADD 100   → total = 104   prev=100
Step 4 → ch = X → curr=10     prev=100   10   < 100    → SUB 10    → total = 94    prev=10
Step 5 → ch = M → curr=1000   prev=10    1000 > 10     → ADD 1000  → total = 1094  prev=1000
Step 6 → ch = C → curr=100    prev=1000  100  < 1000   → SUB 100   → total = 994   prev=100
Step 7 → ch = M → curr=1000   prev=100   1000 > 100    → ADD 1000  → total = 1994  ✅

```

## 4️⃣ Algorithm

```
1. Create a hashmap with all 7 Roman symbols and their integer values

2. Initialize:
      total = 0
      prev  = 0

3. Loop through the string from RIGHT TO LEFT:
      a. Get curr = hashmap[current character]
      b. If curr < prev:
            total = total - curr     ← subtraction case
         Else:
            total = total + curr     ← addition case
      c. Set prev = curr

4. Return total
```

## 5️⃣ PSEUDOCODE 📝

```
function romanToInt(s):

    roman_map = {
        'I': 1,   'V': 5,   'X': 10,
        'L': 50,  'C': 100, 'D': 500,
        'M': 1000
    }

    total = 0
    prev  = 0

    for ch in reverse(s):
        curr = roman_map[ch]

        if curr < prev:
            total -= curr
        else:
            total += curr

        prev = curr

    return total
```

### ✅ Hints
- 💡 Did you build the hashmap correctly with all 7 symbols?
- 💡 Are you traversing in reverse?
- 💡 Is the condition curr < prev (not <=)?
- 💡 Are you updating prev at every step?

---

## 🧠 Key Takeaways
- What did I learn from this problem?
- Why did I choose this specific data structure?
