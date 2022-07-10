import re #Regex Module

s = "hi123are559887fine11" #input example

for i in re.findall("\D+|\d+",s):
    print(i[::-1] if i.isalpha() else i,end="")

#input = hi123are559887fine11
#output = ih123era559887enif11

#abc123
#cba123
