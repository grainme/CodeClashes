# One Loop Method : 
L = [1,2,3,8,9]
target = 17
for i in L[::-1]:
    if target - i in L:
        print(i,target-i)
        break
        
        
        
# Two Loops Method :
L = [1,2,3,8,9]
target = 17
for i in L:
    for k in L:
      if i+k==target:
        print(i,k)
        break
