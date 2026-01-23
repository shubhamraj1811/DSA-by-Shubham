"""
🚀 119. Pascal's Triangle II

🤖 Question : Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
⚠️ Difficulty : 🟩Easy
🧩 Topics : Array, Dynamic Programming

🔮 Algorithm :

1. Create a list (array) called row of size rowIndex + 1 and initialize all elements to 0.
2. Set row[0] = 1. (The first element of any row is always 1).
3. Start an outer loop : i = 1 to rowIndex (inclusive). This loop represents which row we are currently building.
4. Inside this loop, start an inner loop : j = from i down to 1 (inclusive).
5. In the inner loop, update the value at row[j] by adding the value to its left: row[j] = row[j] + row[j-1]
6. We update the values right to left.
7. After the outer loop finishes, return row.

💎 TC = O(k^2)
💎 SC = O(k)
"""

def getRow(rowIndex: int) -> list[int]:
    row = [0] * (rowIndex + 1)
    row[0] = 1

    for i in range(1, rowIndex + 1): # Outer loop for each row from 1 to rowIndex
        for j in range(i, 0, -1): # Inner loop from right (i) to left (1)
            row[j] = row[j] + row[j-1]
            
    return row

# Main Code
pascal_row = getRow(3)
print(f"3-th Row : {pascal_row}")
pascal_row = getRow(5)
print(f"5-th Row : {pascal_row}")
pascal_row = getRow(7)
print(f"7-th Row : {pascal_row}")