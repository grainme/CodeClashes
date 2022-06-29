#We can class students using a dictionnary.
#Name grade1,grade2
L={}
for _ in range(2):
    name, grades = input().split(" ")
    avg=sum(map(float,grades.split(",")))/2
    L[name]=avg

Best =max(L,key=L.get)
print(Best,L[Best])
