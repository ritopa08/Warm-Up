'''
1)
 Check all the element of list1 is present in list 2 and check whether the element order is same.
 eg: l = [2,3,4,5,6]
     l1 = [1,2,3,4]
     o/p : False

 eg: [2,3,4,5,6]
     l1 = [2,3,4]
     o/p : True

 eg: [2,3,10,4,5,6]
    l1 = [2,3,4]
    o/p : False

'''


def chk(l1, l2):
  s1 = len(l1)
  s2 = len(l2)
  c = 0
  for i in range(0, s2):
    if(l1[i] == l2[i]):
      c = 1
    else:
      c = 0
  if(c == 1):
    return True
  else:
    return False


n = input()
while(n):
  l1 = list(input())
  l2 = list(input())
  print(chk(l1, l2))
  n = n - 1
