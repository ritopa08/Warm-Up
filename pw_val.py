
#----- Validate the password separated by commas------#

import re
l = []
s=raw_input("Enter sample password: ")
m = s.split(',')
for p in m:
    if len(p)<6 or len(p)>12:
        continue
    else:
       pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
       pass
    l.append(p)
print ("Valid password is: ")
print (",".join(l))
