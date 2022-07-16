
import string
import re
s=string.ascii_uppercase
x = input()
res = "".join(s[s.index(i[2]) - int(i[1])] if i[0] == "<" else s[s.index(i[2]) + int(i[1])] for i in re.findall("(<|>)(\d+)(\D)", x))

print(res)

'''
same Method but longer:

import string
import re
s=string.ascii_uppercase 
x = input()
res=""
for i in re.findall("(<|>)(\d+)(\D)",x):
    if i[0]=="<":
        res+=s[s.index(i[2])-int(i[1])]
    else:
        res+=s[s.index(i[2])+int(i[1])]
print(res)

'''


'''
method 2: 
exec(bytes('潦⁲⁥湩椠灮瑵⤨献汰瑩⤨瀺楲瑮攨摮挽牨漨摲攨ⵛ崱⬩慛㴺湩⡴孥㨱ㄭ⥝⴬嵡敛せ㱝㸢崢⤩','u16')[2:])
'''


''' 1<B ---> A'''
