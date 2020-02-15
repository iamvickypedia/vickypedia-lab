class Account:
    def __init__(self):
        self.__balance = 0
        print("Thank you for openning an Account with us.")
    def deposit(self,amount):
        self.__balance += amount
        print(f"{amount} Deposited in Account")
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Balance less than the amount")
        else:
            self.__balance -= amount
            print(f"{amount} Withdrawn from account")
    def get_balance(self):
        response = """
#########################################################
#                                                       #
#                  Your Balance is                      #
#                    {}                         #
#                                                       #
#                                                       #
#########################################################
        """.format(str(self.__balance).center(10," ")) # make statement in box
        return response


b1 = Account()
while(True):
    choice_text = """
    Please Chose your Action
    1. Check your Balance
    2. Deposit Money
    3. Withdraw Money
    4. Close Account
    """
    #choice = input("Please chose your action\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Close Account\n")
    choice = input(choice_text)
    if choice == '4':
        print("Bye")
        break
    elif choice == '1':
        print(b1.get_balance())
    elif choice == '2':
        amount = input("Enter the amount to deposit\n")
        b1.deposit(int(amount))
    elif choice == '3':
        amount = input("Enter the amount to withdraw\n")
        b1.withdraw(int(amount))
