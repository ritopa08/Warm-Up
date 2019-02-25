'''  Reverse the string in a manner that digits should be put first then the string o/p.

example i/p----- bag has 53 coins
o/p  35 snioc sah gab


'''
import re


def abc(s):
    m = s[::-1]  # reveresing the string
    t = re.search('\d+', m)  # find digits
    x = t.group()
    a = m.replace(x, "")
    c = x + " " + a
    print(c)


s = input()
abc(s)
