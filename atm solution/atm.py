def checkMoney(request,money):
    result = request
    if request > money:
        print("Money is not enough !!\n the request is: {} \n the money is: {}".format(request,money))
    else:
        while request > 0:
            if request >= 100:
                print(100)
                request -= 100
            elif request >= 50 and request < 100:
                print(50)
                request -=50
            elif request >= 20 and request < 50:
                print(20)
                request -= 20
            elif request >= 10 and request < 20:
                print(10)
                request -= 10
            elif request >= 5 and request < 10:
                print(5)
                request -= 5
            elif request >= 2 and request < 5:
                print(2)
                request -= 2
            else:
                print(1)
                request-=1
        print(" the request is: {} \n the money is:"
              " {}\n the remaining money is: {}".format(result,money,(money-result)))
    print("="*100)

checkMoney(399,800);
checkMoney(1000,800);
checkMoney(257,800);