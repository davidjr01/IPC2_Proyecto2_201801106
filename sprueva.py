import re
a="a12ds"

for i in a:
    if re.search(r'\d',i):
        print("si")
    else:
        print("no")
       


