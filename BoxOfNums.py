x=int(input())
y=int(input())
for i in range(1,x+1):
    if i%y==0:
        print(i,end="\n")
    else:
        print(i,end=" ")
        
#input
6
2  
#Output   
1 2
3 4
5 6
