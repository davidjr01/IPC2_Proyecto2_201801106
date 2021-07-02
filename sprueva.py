import re
a="12/11/1212"

if re.match(r'^([0-2][0-9]|3[0-1])(\/)(0[1-9]|1[0-2])\2(\d{4})$',a):
    print("si")
else:
    print("error")


       


