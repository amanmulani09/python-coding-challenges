# variables are dynamic typed

a = 10
a = 'sam'

# print(a) # the type is defined at run time 

# the comparison operators 

# print(8 and 10)
# print(9 or 10)
# print(not False)


# loops

# while loop
n = 1
while n <= 5:
    # print(n)
    n+=1

# for loop

# for i in range(5):
#     print(i+1)

# looping from 2 to 5
# for i in range(2,6): # the last number is not include start + end + 1
#     print(i)

## division & modular 

# print(int(5/2))

# print(10 % 3) 

## list comprehension 

marks = [10,20,30,40,50]

double_marks = [i*2 for i in marks] # [operation + for in loop ]
half_marks = [ int(i /2) for i in marks]
# print(half_marks)


## hash set & getting unique values 

list_with_dups= [1,2,3,4,1,2]

unique_list_set = list(set(list_with_dups))
# print(unique_list_set)

## convert set to list use list() method vise verse for set()

## hashmap 

user = {}

user["name"] = "aman"
user["age"] = 25

# print(user)

# get number of keys in the hashmap 

# print(len(user))

# search a key exist in hashmap 

# print("name" in user)
user.pop("age")
# print(user)

## dict comprehension

my_map = {i:2*i for i in range(0,5)}

# print(my_map)

## looping thorough a map

## simple way 

# for k in my_map:
#     print(k, my_map[k])

## getting all the values 

# for v in my_map.values():
#     print(v)

## getting key and value 

# for k,v in my_map.items():
#     print(k,v)

## tuples (like list but immutable )

cords = (1.002, 0.323, 1.43)
# print(cords)


## class

class LLM:
    
    def __init__(self,name:str) -> None:
        self.name = name
        
    def get_llm_name(self)-> str:
        return self.name
    
openai = LLM("openai")
print(openai.get_llm_name())