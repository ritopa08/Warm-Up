'''
7) write  a function to generate factorial of given number by using importing lib.py contains function definition and we need to call from other file (use import)

'''


#---- importing user defined library-------
import lib

print("Enter the number: ")
n = int(input())
result = lib.fact(n)
print("factorial is: ")
print(result)
