'''
10. write a program to display square for even numbers and cube for odd numbers by using list comprehenssion (take input from the user upto which number he/she want).
'''


#-----function definations-----
def square(num):
    return ("square of", num, "is", num * num)


def cube(num):
    return ("cube of", num, "is", num * num * num)


#------Range of inputs-------
arr = [i + 1 for i in range(int(input()))]
print(arr)


#-------evaluation------------
i = 0
obj = [square(arr[i]) if arr[i] % 2 == 0 else cube(arr[i]) for i in range(len(arr))]

print(obj)
