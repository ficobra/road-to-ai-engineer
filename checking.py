from bank import BankAccount

class CheckingAccount(BankAccount):
    def charge_fee(self, fee: float) -> None:
        if (self.balance - fee) < 0:
            print("Warning: insufficient funds!")
        else:
            self.balance -= fee