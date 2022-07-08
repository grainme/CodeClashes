#Return the result of the mathematical expression given as a parameter.
#To makes things easy, only addition and multiplication operators will be included.
#But be careful! The priority has been switched between those two operators: ADDITION OPERATOR HAS A HIGHER PRIORITY OVER MULTIPLICATION OPERATOR.

# Input : 2*6+9 ---> Output : 30
# Input : 4*2*7+2*5*6 ---> Output : 2160


from math import prod

exp = input().split("*")       # ---> ['2','6+9']
res = 0
L=[]
for i in exp:       #Iterating through the list
  if "+" in i:
    res = sum(list(map(int,i.split("+"))))
    L.append(res)
  else:
    L.append(int(i)
             
print(prod(L))
    
             
#BTW THIS IS NOT THE BEST APPROACH TO THIS PROBLEM :)
