'''
3. write a program to validate the paranthesis
   example:
      valid string:  "[a+b-{(c/d}+a)*c]^2"
      invalid string: "[a+b"*d

'''

def mat(s,p):
    #c=0
    st=[]
    print(s)
    n=len(s)
    for i in range (0,n):
        if s[i] in p:
            st.append(s[i])
    # st=[s[i] for i in range (0,n) if "s[i]" in p]
    print("st:", st)

    if(len(st)%2==0):
        return ("Valid")
    else:
        return ("Invalid")
    # st_r=[st.pop() for _ in range(0,len(st))]
    # print(st_r)
    # for i in range(0,len(st)):
    #     x=st_r.pop()
    #     if st[i]==x:
    #         print(st[i], x)
    #         pass
    #     else:
    #         return ("False")

    # return ("True")






p=['(',')','[',']','{','}']
s=input()
print(mat(s,p))
