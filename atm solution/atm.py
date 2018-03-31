def checkMoney(request,money):
    result = request
    if request > money:
        print("Money is not enough !!\n the request is: {} \n the money is: {}".format(request,money))
    else:
        while request > 0:
            if request >= 100:
                print("give ",100)
                request -= 100
            elif request >= 50:
                print("give ",50)
                request -=50
            elif request >= 20:
                print("give ",20)
                request -= 20
            elif request >= 10:
                print("give ",10)
                request -= 10
            elif request >= 5:
                print("give ",5)
                request -= 5
            elif request >= 2:
                print("give ",2)
                request -= 2
            else:
                print("give ",1)
                request-=1
        print(" the request is: {} \n the money is:"
              " {}\n the remaining money is: {}".format(result,money,(money-result)))
    print("="*100)
    balance = (money - result)
    return balance
balance = 1500
balance = checkMoney(399,balance)
balance = checkMoney(201,balance)
balance = checkMoney(356,balance)
