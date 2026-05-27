def gcd(num1: int, num2: int):
    #calculates the greatest common
    #divisor between two numbers
    gcdlist = list()
    for i in range(1, min(num1, num2) + 1):
        if i % num1 == 0 and i % num2 == 0:
            gcdlist.append(i)
    return max(gcdlist)