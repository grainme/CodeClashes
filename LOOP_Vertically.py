'''
time = int(input())
how much meters gained / year = int(input())
height = int(input()) [in this case 4]

 #
 #
##
##  


This like Tree 01 : [ , ,#,#]
This like Tree 02 : [#,#,#,#]  Imagine them as vertical trees!

so we need to loop through an array vertically smh !

Okay let"s go then !!

'''

L=[]
res=""
t = int(input())
g = int(input())
h = int(input())

for _ in range(h):
    row = input()
    L.append(list(row))
    
# L = [[' #'], [' #'], ['##'], ['##']] ---> or [[' #']
#                                              ,[' #'], 
#                                               ['##'], 
#                                               ['##']]

# print(list(zip(*L))) --> Output:  [(' ', ' ', '#', '#'), ('#', '#', '#', '#')]

res=""
for i in list(zip(*L)):
    res+= str(t*g + i.count("#")) + " "
    
print(res.rstrip())
