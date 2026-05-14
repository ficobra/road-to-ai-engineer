from bank import BankAccount

class CheckingAccount(BankAccount):
    def charge_fee(self, fee: float) -> None:
        if (self.balance - fee) < 0:
            print("Warning: insufficient funds!")
        else:
            self.balance -= fee

acc = CheckingAccount("Filip")
acc.deposit(200)
acc.charge_fee(15)
print(acc.get_balance())  # 185.0

acc.charge_fee(200)  # Warning: insufficient funds!
print(acc.get_balance())  # Still 185.0