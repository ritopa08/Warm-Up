''' Get the values of X and Y dynamically and generate a 2 D array.(nested list)
Example if you take the input as 2,3 then the o/p should be
[[1,2,3].[1,4,,9]] ----- The values to put inside are of your choice.


'''


def arr(m, n):
    l = []
    p = []
    for i in range(0, m):
        for j in range(0, n):
            l.append(int(input()))
        p.append(l)
        l = []
    return p


m = int(input())
n = int(input())

print(arr(m, n))
