import re

sen = "Love is in the air "

x = re.findall("adi",sen)
print(x)

if (x):
    print("Yes there is at leas one match! ")
else:
    print("No match")
    
