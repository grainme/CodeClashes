
c=0
a=""
n = input() # Letter to track
t = input() # String

for i in t: 
    if i == n: 
        c+=1
    else:
        if c>0:
            a+=str(c)
            c=0
        a+=i
if c>0:
    a+=str(c)
print(a)


# Input : t = Hello World  ;; n = l --> Output : he2o Wor1d
