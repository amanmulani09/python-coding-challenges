
## a blueprint - used to create instace / objects which has the same attributes and access for the methods
class Waiter:
    tables = []
        
raj = Waiter()
simran = Waiter()

## the __init__ method ?? 

# init method is used to avoid the data overlapping, sharing between the class instances, \\
    
# self helps to keep the data of each object separate to operate and use 


class SmartWaiter:
    
    def __init__(self,name:str) -> None:
        self.tables:list[str] = []
        self.name = name
        
    def take_order(self):
        print(self.name, "is taking order")
        
    def add_table(self,table_number:str):
        self.tables.append(table_number)

raj = SmartWaiter("raj")
# raj.take_order()
simran = SmartWaiter("simran")
# simran.take_order()

raj.add_table("id_1")
raj.add_table("id_2")

print(raj.tables)

## encapsulation -> object holding their own data and state!


