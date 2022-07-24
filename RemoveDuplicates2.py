s = input()[::-1]
t = []
for i in range(len(s)):
    if s[i] not in t:
        t.append(s[i])
print(''.join(t[::-1]))
