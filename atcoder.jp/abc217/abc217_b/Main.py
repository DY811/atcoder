a = []
for i in range(3):
    tmp = input()
    a.append(tmp)
#print(a)

d = ["ABC" , "ARC" , "AGC" , "AHC"]

for i in range(4):
    if d[i] not in a:
        print(d[i])

