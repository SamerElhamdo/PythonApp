class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdraw_history = []

    def withdraw(self, request):
        print("welcome to: {}\nCurrent balance: {}".format(self.bank_name, self.balance))
        print("="*50)
        result = request
        if request > self.balance:
            print("Money is not enough !!\n the request is: {} \n the money is: {}".format(request, self.balance))
        elif request <= 0:
            print("More than zero plz!")
        else:
            self.withdraw_history.append(request)
            while request > 0:
                if request >= 100:
                    print("give ", 100)
                    request -= 100
                elif request >= 50:
                    print("give ", 50)
                    request -= 50
                elif request >= 20:
                    print("give ", 20)
                    request -= 20
                elif request >= 10:
                    print("give ", 10)
                    request -= 10
                elif request >= 5:
                    print("give ", 5)
                    request -= 5
                elif request >= 2:
                    print("give ", 2)
                    request -= 2
                else:
                    print("give ", 1)
                    request -= 1
            print("the request is: {} \nthe money is:"
                  " {}\nthe remaining money is: {}".format(result, self.balance, (self.balance - result)))
        print("=" * 50)
        self.balance = (self.balance - result)
        return self.balance
    def show_withdrawals(self):
        for withdrawal in self.withdraw_history:
            print("from {} ckeck money {}".format(self.bank_name,withdrawal))

balanc1 =600
balanc2 = 1200
atm1 = ATM(balanc1, "bank albaraka")
atm2 = ATM(balanc2, "bank ziraat")
atm1.withdraw(559)
atm1.withdraw(440)
atm2.withdraw(685)
atm2.withdraw(254)
atm1.show_withdrawals()
atm2.show_withdrawals()