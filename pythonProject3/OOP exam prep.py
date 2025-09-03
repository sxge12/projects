class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def poop(self):
        print(f"{self.name} pooped! ")

    def info(self):
        print(f"{self.name} is {self.age} years old")

dog1 = dog("buddy", 9)

z = dog1.poop()
#print(z)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print(f"Cannot withdraw. Current balance: ${self.balance}")
        else:
            print("withdrawal amount must be positive.")


    def current_balance(self):
        print(f"current balance : ${self.balance}")


class savingsaccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate/100)
        self.balance += interest
        print(f"your new balance after accrued interest is. Balance: ${self.balance}")






class fruit():
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def juice(self):
        print(f" you have juiced {self.name}")

    def slice(self):
        print(f"you sliced {self.name} and {self.colour}ed juice came out")


fruit1 = fruit("gabagaba fruit", "yellow")

print(fruit1.slice())


Account1 = BankAccount("presh", 2000)

z = Account1.current_balance()

#print(z)