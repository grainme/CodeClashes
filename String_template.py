import sys
import math


s = input()
f = input()

res = ""
i = 0
for c in f:
    if c == "X":
        res += s[i].upper()
        i += 1
    elif c == "x":
        res += s[i].lower()
        i += 1
    else:
        res += c

print(res)

#hElloMarouane 
#Xxxxx, XXXXXXXX   ---> output: Hello, MAROUANE
