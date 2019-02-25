'''
9) write a program to display the which day you born ?(take dob as input from the user)
'''


from datetime import *

# Today's Date
today = date.today()
print("Today: " + today.strftime('%A %d, %b %Y'))

dob_str = input("Enter your Date of Birth (dd/mm/yyyy) : ")
dob_data = dob_str.split("/")
dobD = int(dob_data[0])
dobM = int(dob_data[1])
dobY = int(dob_data[2])
dob = date(dobY, dobM, dobD)
print(dob)

day = dob.strftime("%A")
print("You were born on  " + day + ".")
