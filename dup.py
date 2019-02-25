'''  Remove duplicates and sort the words in a para

eg. The values that we got are the same values
o/p: are got same that the values we.


'''


def abc(s):
    k = []
    str1 = " "

    #----removing duplicates-------
    s = s.lower()
    slist = s.split()
    t = " ".join(sorted(set(slist), key=slist.index))

    #-------Sorted in alphabetically----
    m = t.split()
    m.sort()

    #-----sorted unique words
    for word in m:
        k.append(word)
    print(str1.join(k))


s = input()
abc(s)
