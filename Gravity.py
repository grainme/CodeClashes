lines = int(input())
ar = [[] for _ in range(lines)]
for _ in range(lines):
    row = input()
    for k in range(len(row)):
        if row[k] != "|":
            ar[k] = row[k]
print("".join(ar))

#A|||
#||B|
#|C||    --> ACBD
#|||D
