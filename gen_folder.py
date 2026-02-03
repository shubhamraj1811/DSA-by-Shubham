import os

def get_difficulty_info(difficulty_raw):
    """Returns the emoji and formatted string based on input."""
    diff = difficulty_raw.strip().lower()
    if diff == "easy":
        return "🟢 Easy", "Easy"
    elif diff == "medium":
        return "🟠 Medium", "Medium"
    elif diff == "hard":
        return "🔴 Hard", "Hard"
    else:
        return "⚪ Unknown", "Unknown"

def update_readme(prob_num, prob_name, diff_display, folder_path):
    readme_path = "README.md"
    # Format: | # | Problem Name | Difficulty | Solution |
    new_row = f"| {prob_num} | [{prob_name.replace('-', ' ')}](./{folder_path}/solution.py) | {diff_display} | [View Approach](./{folder_path}/approach.md) |\n"
    
    if os.path.exists(readme_path):
        with open(readme_path, "a", encoding="utf-8") as f:
            f.write(new_row)
        print(f"✅ Updated README.md with {diff_display} Problem {prob_num}")
    else:
        print("❌ README.md not found.")

def create_dsa_template():
    # 1. Inputs
    prob_num = input("Enter Problem Number (e.g., 1): ").strip().zfill(4)
    prob_name_raw = input("Enter Problem Name: ").strip()
    prob_name_slug = prob_name_raw.replace(" ", "-")
    difficulty_input = input("Enter Difficulty (easy/medium/hard): ")
    topics = input("Enter Topics (e.g., Array, Hash Table): ").strip()
    
    # Get Emoji formatting
    diff_display, diff_simple = get_difficulty_info(difficulty_input)
    
    folder_path = f"LeetCode/{prob_num}-{prob_name_slug}"
    
    # 2. Create Folder
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        print(f"⚠️ Folder {folder_path} already exists!")
        return

    # 3. Define the detailed problem.md content
    problem_md_content = f"""# Problem {prob_num}: {prob_name_raw}

[LeetCode Link](https://leetcode.com/problems/{prob_name_slug.lower()}/)

⚒️ **Difficulty:** {diff_display}
🎓 **Topics:** {topics}

### Problem Statement

### Example 1:
**Input:**
**Output:**
**Explanation:**

### Constraints:

---------------
"""

    # 4. Create Files
    files = {
        "problem.md": problem_md_content,
        "approach.md": f"# Approach for {prob_name_raw}\n\n## 💡 Intuition\n\n## ⚙️ Algorithm\n\n## 📊 Complexity\n- Time: $O()$\n- Space: $O()$",
        "solution.py": "class Solution:\n    def solve(self, nums):\n        pass",
        "testsolution.py": f"import unittest\nfrom solution import Solution\n\nclass TestSolution(unittest.TestCase):\n    def test_case_1(self):\n        sol = Solution()\n        # self.assertEqual(sol.solve(), expected)\n\nif __name__ == '__main__':\n    unittest.main()"
    }

    for filename, content in files.items():
        with open(os.path.join(folder_path, filename), "w", encoding="utf-8") as f:
            f.write(content)
    
    # 5. Auto-Update README
    update_readme(prob_num, prob_name_raw, diff_display, folder_path)

if __name__ == "__main__":
    create_dsa_template()