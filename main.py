from bank_account import BankAccount

def main():
    # account1 = BankAccount("Alex", 1000)
    # account1.set_balance(2000)
    #
    # print(account1)

    a1 = BankAccount("Alex", 1000)
    print(a1.balance)
    print(a1._balance)
    print(a1.)
    a1.balance += 1000
    print(a1.balance)
    del a1.balance
main()
