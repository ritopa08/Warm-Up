'''
11.Write a program to read the text from the file and reverse it and write into file.
ex : input: hai hello
   output : iah olleh
'''

#----importing RE library----
import re

#----creating file-------
f = open("abc.txt", 'w')
f.write("hai hello")
f.close()


#------Performing operations on the file------
f = open("abc.txt", 'r+')
s = f.read()
l = []
lst = re.split('[" " \n]', s)
for i in lst:
    l.append(i[::-1])
print(" ".join(l))
