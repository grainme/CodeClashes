#Rotation number
#123456789 => 456789123  
#1 => 4
#2 => 5
#  ...
#9 => 3


# Example : Input = 123 ----> Output = 456

##### MY SOLUTION :

l = input()
s=""
for i in l:
    x=int(i)+3
    s += str(x) if x<10 else str(x%10+1)
print(r)


#### AUTHOR'S SOLUTION : 
l = input()
res=""
for i in l:
    res+="456789123"[int(i)-1]
print(res)



# Problem's Link : https://www.codingame.com/contribute/view/1298578cda5354395e5a51f07f8dd7c0dca54
