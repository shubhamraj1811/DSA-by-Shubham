"""
🚀 118. Pascal's Triangle I

🤖 Question : Given an integer numRows, return the first numRows of Pascal's triangle.
⚠️ Difficulty : 🟩Easy
🧩 Topics : Array, Dynamic Programming
🏢 Companies : Amazon, Adobe

🔮 Algorithm : Row-by-Row Dynamic Programming

1. If numRows == 0 → return []
2. Initialize result = [[1]]  // Row 0
3. For i from 1 to numRows-1:
     a. Create new_row = [1]  // First element
     b. For j from 1 to i-1:
          new_row.append(prev_row[j-1] + prev_row[j])
     c. new_row.append(1)  // Last element
     d. Append new_row to result
     e. Set prev_row = new_row
4. Return result

💎 Time Complexity : O(numRows²)
💎 Space Complexity : O(numRows²)  // Storing full triangle
"""

from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []

    result = [[1]]  # Row 0

    for i in range(1, numRows):
        prev_row = result[-1]
        new_row = [1]  # Start with 1
        # Middle elements
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        # add last element
        new_row.append(1)  # End with 1
        result.append(new_row)

    return result

# Main Code
num = int(input("Enter number of rows: "))
pascal = generate(num)

print(f"\nPascal Triangle of {num} rows are: \n")
for rows in pascal:
    print(rows)