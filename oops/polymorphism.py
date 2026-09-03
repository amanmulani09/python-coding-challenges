
## having a different behaviour of same method - calls polymorphism - prefers the 
# poly - means many - many form of a method 
# one class passes it's data and method to another class damn inheritance
class Staff:
    
    def __init__(self, name:str, shift:str) -> None:
        self.name = name
        self.shift = shift
        
    def start_work(self):
        print(f"{self.name} starts work on {self.shift} shift")
    
    def work(self):
        print(f"{self.name} is working")
        

class Waiter(Staff):
    
    def take_order(self):
        print(f"{self.name} is taking an order")
        
    def work(self):
        self.take_order()
        
class Chef(Staff):
    
    def cook_food(self):
        print(f"{self.name} is cooking food")
        
    def work(self):
        self.cook_food()

        
raj = Waiter("Raj","Morning")
simran = Chef("simran","afternoon")

raj.work()
simran.work()
