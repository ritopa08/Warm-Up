import re

file = open('info.txt', 'r+')
data = file.read()
X = '([a-fA-F0-9]{2}[:|\-]?){6}'
Y = '[0-9]+(?:\.[0-9]+){3}'
a = re.compile(X).search(data)
b = re.compile(Y).search(data)
if a:
    print(data[a.start(): a.end()])
if b:
    print(data[b.start(): b.end()])
