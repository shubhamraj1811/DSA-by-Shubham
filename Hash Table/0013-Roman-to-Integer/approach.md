# Approach: Roman to Integer

## The Roman Number System
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

### The Subtraction Rule ⚠️ (The Tricky Part!)
* Normally, Roman numerals are added left to right.
* But when a smaller value appears BEFORE a larger value → it gets subtracted!

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

### Examples:

```
Input: s = "III"    → 1+1+1         = 3
Input: s = "LVIII"  → 50+5+1+1+1   = 58
Input: s = "MCMXCIV"→ 1000+900+90+4 = 1994
       M  CM  XC  IV
       ↑  ↑   ↑   ↑
      add sub sub sub
```

## 💡 Intuition
### Method 1: Brute Force / Initial Idea
### Method 2: Optimized Approach

## ⚙️ Algorithm

## 📊 Complexity
- **Time Complexity:** $O()$
- **Space Complexity:** $O()$

---

## 🧠 Key Takeaways
- What did I learn from this problem?
- Why did I choose this specific data structure?
