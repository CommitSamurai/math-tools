#checks to see if a number is prime
def prime_checker(num: int):
    divisors = list()
    for i in range(1, num + 1):
        if (num % i == 0):
            divisors.append(i)
    if len(divisors) == 2:
        return 'Prime'
    else:
        return 'Not prime'
    