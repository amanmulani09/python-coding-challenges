class BankAccount:
    def __init__(self, owner:str, balance:int):
        self.owner = owner            # Public attribute
        self._account_type = "Checkings" # Protected attribute (convention only)
        self.__balance:int = balance      # Private attribute (triggers name mangling)

    # Getter method: Safely view the private balance
    def get_balance(self):
        return self.__balance

    # Setter method: Safely update the balance with business logic validation
    def deposit(self, amount:int):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

# --- Interacting with the Object ---
account = BankAccount("Alice", 1000)