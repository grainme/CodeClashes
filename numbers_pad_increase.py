#Rotation number
#123456789 => 456789123  
#1 => 4
#2 => 5
#  ...
#9 => 3


# Example : Input = 123 ----> Output = 456

##### MY SOLUTION :

l = input()
r=""
for i in l:
    x=int(i)+3
    if x<10:r+=str(x)
    else:r+=str(x%10+1)
print(r)
