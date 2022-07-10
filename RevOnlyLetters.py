import re

s = "hi123are559887fine11"
matches = re.findall("(\D+)(\d+)",s)
for i in matches:
    for k in i:
        if k.isalpha():
            print(str(k)[::-1],end="")
        else:
            print(k,end="")

#input = hi123are559887fine11
#output = ih123era559887enif11

#abc123
#cba123
