a,b,c = list(map(int,input().split()))
d = int(input())

L = ["+","-","*","/"]
M = []
for i in range(4):
    for k in range(4):
        if (eval(a+L[i]+b+L[k]+c) == d):
            M.append(a+L[i]+b+L[k]+c)
print(M)
