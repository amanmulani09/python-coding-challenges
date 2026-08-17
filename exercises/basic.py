
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
