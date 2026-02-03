# Approach for Two Sum

## 💡 Intuition

### The Brute Force Method
In the brute force method, we can just take a number and check for its partner in the rest of the array. This will take O(n^2) time.

But a better solution exists for this problem, the Hashmap method.

### The Hash Map Method
In the Hashmap, what we do is when we encounter a number we check it with the target, if it isnt it, we save it in the hashtable and then look forward.
Its similar to checking the notebook if the complement exist.

## ⚙️ Algorithm
1. Initialize an empty hash map (dictionary) where the key is the number and the value is its index.
2. Iterate through the array using both the index i and the value n.
3. Calculate the complement : `diff = target - n`.
4. Check the map:
   1. If diff is already in the hash map, Pair dound! Return the index stored in the map and the current index i.
   2. If diff is NOT in the hash map, Add the current number n and its index i to the hash map.
5. If the loop finish without finding a pair, means no solution exists in the array.

## 📊 Complexity
- Time: $O(n)$ = We only pass through the list once, and Hash Map lookups are $O(1)$ on average.

- Space: $O(n)$ = In the worst case, we might store almost all elements in the Hash Map before finding the pair.