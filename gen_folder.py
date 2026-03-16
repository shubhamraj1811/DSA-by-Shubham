import os

def get_difficulty_info(difficulty_raw):
    """Returns the emoji and formatted string based on input."""
    diff = difficulty_raw.strip().lower()
    mapping = {
        "easy": ("🟢 Easy", "Easy"),
        "medium": ("🟠 Medium", "Medium"),
        "hard": ("🔴 Hard", "Hard")
    }
    return mapping.get(diff, ("⚪ Unknown", "Unknown"))

def update_readme(prob_num, prob_name, diff_display, topics, folder_path):
    """Updates the root README.md with an enhanced table layout."""
    readme_path = "README.md"
    
    # FIX: Added a newline character (\n) at the very end of the row
    new_row = f"| {prob_num} | [{prob_name}](./{folder_path}/problem.md) | {diff_display} | `{topics}` | [🐍 Solution](./{folder_path}/solution.py) |\n"
    
    # Initialize README if it doesn't exist
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write("# LeetCode Solutions Portfolio\n\n")
            f.write("| # | Problem Name | Difficulty | Topics | Solution |\n")
            f.write("|---|---|---|---|---|\n")

    # Open in append mode
    with open(readme_path, "a", encoding="utf-8") as f:
        # Extra safety: Ensure we are starting on a new line by checking file end
        f.write(new_row)
    
    print(f"✅ README.md updated successfully.")

def create_dsa_template():
    # --- 1. User Inputs ---
    prob_num = input("🔢 Problem Number: ").strip().zfill(4)
    prob_name_raw = input("📝 Problem Name: ").strip()
    category = input("📁 Category (e.g., Arrays, DP, Graphs): ").strip().title()
    difficulty_input = input("⚖️ Difficulty (easy/medium/hard): ")
    topics = input("🏷️ Specific Topics: ").strip()
    
    # Formatting slugs and paths
    prob_name_slug = prob_name_raw.lower().replace(" ", "-")
    diff_display, _ = get_difficulty_info(difficulty_input)
    
    # Folder Path
    folder_path = f"{category}/{prob_num}-{prob_name_slug}"
    
    # --- 2. Create Directory Structure ---
    if os.path.exists(folder_path):
        print(f"⚠️ Folder '{folder_path}' already exists! Skipping...")
        return
    
    os.makedirs(folder_path)

    # --- 3. Define File Templates ---
    
    approach_content = f"""# Approach: {prob_name_raw}

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
"""

    problem_md_content = f"""# Problem {prob_num}: {prob_name_raw}

[🔗 LeetCode Link](https://leetcode.com/problems/{prob_name_slug}/)

⚒️ **Difficulty:** {diff_display}
🎓 **Topics:** {topics}

---

### 📝 Problem Statement

---

### 📥 Example 1
**Input:**
**Output:**
**Explanation:**

---

### ⚠️ Constraints
- 
"""

    solution_py_content = f"""# Problem: {prob_name_raw}
# Category: {category}

class Solution:
    def solve(self, nums):
        # Implementation goes here
        pass

        return()
"""

    test_solution_content = """from solution import Solution

def run_tests():
    sol = Solution()

    # (input_data, expected_output)
    test_cases = [
        ((), ()),
        ((), ()),
    ]
    
    for i, (data, expected) in enumerate(test_cases):
        # result = sol.solve(data)
        # print(f"Test Case {i+1}: {'✅ Pass' if result == expected else '❌ Fail'}")
        print(f"Test Case {i+1} initialized.")

if __name__ == '__main__':
    run_tests()"""

    # --- 4. Write Files ---
    files = {
        "problem.md": problem_md_content,
        "approach.md": approach_content,
        "solution.py": solution_py_content,
        "testsolution.py": test_solution_content
    }

    for filename, content in files.items():
        with open(os.path.join(folder_path, filename), "w", encoding="utf-8") as f:
            f.write(content)
    
    # --- 5. Update Portfolio Index ---
    update_readme(prob_num, prob_name_raw, diff_display, topics, folder_path)
    print(f"\n🚀 Project structure created in: {folder_path}")

if __name__ == "__main__":
    create_dsa_template()