s = 'abbcccda'

olds = []
for c in s:
    if olds and c in olds[-1]:
        olds[-1].append(c)
    else:
        olds.append([c])
print(olds)
res = ''.join([f'{lst[0]}{len(lst)}' for lst in olds])
print(res)

#  [['a'], ['b', 'b'], ['c', 'c', 'c'], ['d'], ['a']]
#  a1b2c3d1a1
