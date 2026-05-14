from bank import BankAccount, SavingsAccount

acc1 = BankAccount("Ana")
acc1.deposit(1000)
acc1.withdraw(400)

acc2 = SavingsAccount("Filip")
acc2.deposit(500)
acc2.apply_interest(5)

print(acc1.get_balance())  # 600.0
print(acc2.get_balance())  # 525.0