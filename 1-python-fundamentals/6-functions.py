def sayHello(name='Sam'):
    """
    Print Hello and then name.
    """
    print('Hello '+name)


sayHello('Sam')
sayHello('Beth')
sayHello()


def getSum(num1, num2):
    total = num1+num2
    return total


numSum = getSum(6, 100)
print(numSum)


def addOneToNum(num):
    num += 1
    return num


num = 5
new_num = addOneToNum(num)
print(new_num)


def getSum(num1, num2): return num1+num2


print(getSum(9, 2))


def addNumToOne(num): return num+1


print(addNumToOne(5))
