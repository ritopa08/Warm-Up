''' Create a dictionary with number and its square from 19 to 31


'''

m = int(input())
n = int(input())
sq = {x: x * x for x in range(m, n)}
print(sq)
