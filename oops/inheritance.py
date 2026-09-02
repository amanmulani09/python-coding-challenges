
# one class passes it's data and method to another class damn inheritance
class Staff:
    
    def __init__(self, name:str, shift:str) -> None:
        self.name = name
        self.shift = shift
        
    def start_work(self):
        print(f"{self.name} starts work on {self.shift} shift")
        

class Waiter(Staff):
    
    def take_order(self):
        print(f"{self.name} is taking an order")
        
class Chef(Staff):
    
    def cook_food(self):
        print(f"{self.name} is cooking food")
        
raj = Waiter("Raj","Morning")
simran = Chef("simran","afternoon")

raj.take_order()
simran.cook_food()
