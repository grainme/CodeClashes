#this code ensure if the user's input is a perfect number or not and then gives a list of them. 
# 6 is a perfect number because 6=3*2*1 and 3+2+1=6 ) 

def is_perfect(x):
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum+=i
    if sum==x:
        return True
    else:
        return False
    
#print(is_perfect(int(input("Type a Number: "))))

list=[]
for i in range(1,pow(10,3)):
    if is_perfect(i):
        list.append(i)
        
print(list)    
