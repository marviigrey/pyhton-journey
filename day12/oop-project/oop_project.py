from bank_accounts import *

Dave = BankAccount(1000, "Marvellous")
chika = BankAccount(100000, "chika")

Dave.getBalance()
chika.getBalance()

Dave.deposit(500)
chika.deposit(50000)

chika.withdraw(100)
Dave.withdraw(100)

chika.transfer(1000, Dave)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAccount(1000, "Blaze")

Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000, chika)
