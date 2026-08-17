
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

