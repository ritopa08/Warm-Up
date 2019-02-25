
#---------sorting elements without using predefined function--------------#

l = list(input())  #enter elements without using separator
print(l)
n = len(l)
for i in range(n):
    for j in range(1, n-i):
        if l[j-1] > l[j]:       #arranging in ascending order
            (l[j-1], l[j]) = (l[j], l[j-1])
print(l)
