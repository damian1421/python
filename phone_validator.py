import re

#your code goes here

number = input() 

x = re.search(r"[1|8|9][0-9]{7}$", number)

if x:
    print ("Valid")
else:
    print ("Invalid")
