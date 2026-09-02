
"""
Practice Problem: Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, 
return their product; otherwise, return their sum.
"""

def get_product(first:int,second:int) -> int:
    
    product = first * second
    
    if product <= 1000:
        return product
    else:
        return first + second
    
# print(get_product(20,30))
# print(get_product(40,30))

# ------------------------------------------------------------------------------------------

"""
Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration, 
print the current number, the previous number, and their sum.
"""

def get_range(num:int) -> None:
    
    prev_num = 0
    for i in range(0, num):
        sum = prev_num + i
        print(f"current : {i} prev: {prev_num} sum : {sum} ")
        prev_num = i
        
# get_range(10)

# ------------------------------------------------------------------------------------------

"""
Practice Problem: Display only those characters which are present at
an even index number in given string.
"""

def modify_str(s:str):
    if(len(s) < 1):
        return ''
    for index,v in enumerate(s):
       if(index % 2 == 0):
           print(v)

nums = [1,2,3,4,5,6,7,8,9,10]

def travers_list(nums:list[int])->None:
    
    for i,v in enumerate(nums):
        if i % 2 == 0:
            print(v)
            
# travers_list(nums)

# ------------------------------------------------------------------------------------------

"""
Practice Problem: Write a function to remove characters from a string starting from
index 0 up to n and return a new string.
"""
# substring = s[start : end : step]
def subs_tring(s:str,start:int)-> str:
    return s[start:]

# print(subs_tring("pynative",2))

# ------------------------------------------------------------------------------------------

# Exercise 5. Variable Swapping (The In-Place Method)

a = 10
b = 20
# print(f'before:  {a},{b}')
a,b = b,a
# print(f'before:  {a},{b}')

# ------------------------------------------------------------------------------------------

# Exercise 6. Calculating Factorial with a Loop

def calc_factorial(n:int,factorial:int=1):
    
    for i in range(1, n + 1):
        factorial  = factorial* i
    print(factorial)    

# calc_factorial(5)

# ------------------------------------------------------------------------------------------

"""
Practice Problem: Create a list of 5 fruits. Add a new fruit to the end of the list,
then remove the second fruit (at index 1).
"""

fruits = ["apple","banana","grapes","papaya","orange"]

fruits.append("mango")
fruits.pop(1)
# print(fruits)

# ------------------------------------------------------------------------------------------

"""
Practice Problem: Write a program that takes a string and reverses it 
(e.g., “Python” becomes “nohtyP”).
"""

def reverse_str(s:str)->str:
    return s[::-1]

# print(reverse_str("aman"))

def reverse_str_loop(s:str)->str:
    output = ''
    for i in range(len(s)-1, -1, -1):
        output+=s[i]
    return output

# print(reverse_str_loop("aman"))

# ------------------------------------------------------------------------------------------
"""
Practice Problem: Write a program to count the total number of vowels
(a, e, i, o, u) present in a given sentence.
"""

def get_vowels_count(sentense:str) -> int:
    
    vowels = 'aeiou'
    count = 0
    for char in sentense.lower():
        if char in vowels:
            count+=1
    return count

# print(get_vowels_count("Learning Python is fun!"))

# ------------------------------------------------------------------------------------------

# Practice Problem: Given a list of integers, find and print both the largest and the smallest numbers.

def get_min_max_num(nums:list[int]):
    
    min = nums[0]
    max = nums[0]
    
    for num in nums:
        if(num <= min):
            min = num
        if (num >= max):
            max = num
            
    return {
        "Smallest":min,
        "Largest":max
    }
    
# print(get_min_max_num([45, 2, 89, 12, 7]))

def get_min_max_method(nums:list[int]):
    
    smallest = min(nums)
    largest = max(nums)
    
    return {
        "Smallest":smallest,
        "Largest":largest
    }

# print(get_min_max_method([45, 2, 89, 12, 7]))

# ------------------------------------------------------------------------------------------

# Exercise 11. Removing Duplicates from a List

def remove_duplicate(numlist:list[int]) -> list[int]:
    
    temp = []
    
    for item in numlist:
        if item not in temp:
            temp.append(item)
    
    return temp

# print(remove_duplicate([1, 2, 2, 3, 4, 4, 4, 5]))

# ------------------------------------------------------------------------------------------

# Exercise 12. List Comparison and Boolean Logic

"""
Practice Problem: Write a function to return True if the first and last number of a
given list is the same. If the numbers are different, return False.
"""

def check_first_and_last_item(items:list[int]) -> bool:
    
    return items[0] == items[-1]


# print(check_first_and_last_item([10, 20, 30, 40, 10]))
# print(check_first_and_last_item([75, 65, 35, 75, 30]))

# ------------------------------------------------------------------------------------------