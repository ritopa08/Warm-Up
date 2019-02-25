import re
s = " "
file = open('info.txt', 'r+')
data = file.read()
X = "^(?=.*[^\.]$)((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.?){4}$"

a = re.compile(X).search(data)
if a:
    s = (data[a.start(): a.end()])
file.close()

data = data.replace(s, "ff:ff:ff:ff:ff:ff")

file = open('new.txt', 'w+')
file.write(data)
file.close()
