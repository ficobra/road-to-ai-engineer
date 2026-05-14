class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if (self.balance - amount) < 0:
            print("Warning: insufficient funds!")
        else:
            self.balance -= amount

    def get_balance(self) -> float:
        return self.balance
    
class SavingsAccount(BankAccount):
    def apply_interest(self, rate: float) -> None:
        self.balance += (rate * self.balance / 100)
