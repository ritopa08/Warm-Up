#------------factorial without recursion------------------#
n = int(input())
fact = 1

for i in range(1,n+1):
    fact = fact * i

print ("The factorial is : ",end="")
print (fact)

#------------factorial with recursion------------------#
def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

n = int(input())
if n < 0:
   print("Invalid!!!!")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",n,"is",fact(n))
