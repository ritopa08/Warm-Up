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


from plot import Plot, PI

#--- Derived class-----


class Circle(Plot):
    def __init__(self, name, radius):
        Plot.__init__(self, name)
        self.data = ["Radius: ", radius]
        self.circumference = 2. * PI * radius

    def showcircum(self):
        return(self.circumference)


c = Circle("Circumference of a circle is: ", 30)
print(c.showname(), c.showcircum())
