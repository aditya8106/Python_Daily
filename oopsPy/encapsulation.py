## encapsulation example 

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

a=BankAccount("123456789", 1000)
a.__balance = 2000
print(a.get_balance())  # This will raise an AttributeError because __balance is private


a._BankAccount__balance = 2000  # Accessing the private attribute using name mangling
print(a.get_balance())  # This will print 2000, but it's not recommended to access private attributes this way.

"""here Abstraction means we can use the methods of the class without knowing how they are implemented. For example, we can call the deposit and withdraw methods without knowing how they work internally. We just need to know what they do and how to use them. This is an example of abstraction in object-oriented programming.""" 
""" in this example, the BankAccount class encapsulates the balance attribute and provides public methods to interact with it. The user of the class does not need to know how the balance is stored or updated; they just use the deposit and withdraw methods. This is an example of abstraction in object-oriented programming."""