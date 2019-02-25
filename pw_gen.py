import random
import string


c = 0
n = int(input("maximum length of the password: "))
pwd = ""


while c != n:

    u_case = [random.choice(string.ascii_uppercase)]
    l_case = [random.choice(string.ascii_lowercase)]
    sym = [random.choice(string.punctuation)]
    num = [random.choice(string.digits)]

    password = u_case + l_case + sym + num  # list of choices
    pwd += random.choice(password)  # randomly select anyone from choice
    c += 1
    continue

exp = ['@', '%', '$']  # list of exception symbols
if len(pwd) == n:
    print(pwd)
    for i in range(len(pwd)):      # validating the random pwd
        if pwd[i] in exp:
            print("Invalid password!!!!")
        else:
            pass
