# import math


# def fact(n):
#     result = math.factorial(n)
#     return result


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
