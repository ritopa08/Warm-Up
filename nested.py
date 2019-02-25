#-------- using nested loop find second lowest scorer----#


a=[]
d=[]
b=[]
for _ in range(int(input())):  # user input for marks and name
    name = input()
    score = float(input())
    a=[name,score]
    d.append(a)
#print(d)
for i in d:
    m=sorted(d,key=lambda x: x[0])  #sorted by name
    #m=sorted(m,key=lambda x: x[1])  #sorted by marks

#print (m)
for k in m:
    b.append(k[1])

d=b
l=set(d)
l=sorted(list(l))
#print(l)
b=l[1]
#print(b)

for j in m:
    if(j[1]==b):
        c=j[0];
        print("second lowest number is ",b,"scored by",c)
