'''

6)  write a sample program with inheritence, file importing and accessing methods in a class from another file ( imported file)
eg:
file1.py:
class class1:
   def func1:
   def func2:

file2.py:
import file1.py and use the methods in that.
class class2:
    # use methods of file1
'''


import math
PI = math.pi

#----- Base class-----


class Plot:
    def __init__(self, name):
        self.name = name

    def showname(self):
        return(self.name)
