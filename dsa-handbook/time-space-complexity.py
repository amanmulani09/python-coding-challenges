"""
⏱️ 3. Time Complexity (Core Idea)

Count how many operations your code performs as n grows.

Not actual seconds.
We measure growth rate.

things to calculate the time complexity 

1. always consider wrost case scenario
2. avoid constant values 
3. avoid lower values 

different types of time complexity

1. Big O -> wrost case 
2. theta(0) -> average case
3. Omeaga -> best case 

always focus on Big O


🔹 Example 1: O(1) — Constant Time

def get_first(arr):
    return arr[0]
    
Always 1 operation
Doesn't depend on n

👉 Time Complexity = O(1)

🔹 Example 2: O(n) — Linear Time
def print_all(arr):
    for num in arr:
        print(num)
Runs n times

👉 Time Complexity = O(n)

🔹 Example 3: O(n²) — Nested Loops
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
Outer loop: n
Inner loop: n

👉 Total = n × n = O(n²)


🔹 Example 4: O(log n) — Binary Search Thinking
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

Each step cuts input in half.

👉 Time Complexity = O(log n)

🧮 4. How to Calculate Time Complexity (Step-by-Step)
Step 1: Identify loops
Step 2: Count iterations
Step 3: Multiply if nested
Step 4: Ignore constants


🧠 5. Space Complexity (Core Idea)

How much extra memory your algorithm uses.
"""