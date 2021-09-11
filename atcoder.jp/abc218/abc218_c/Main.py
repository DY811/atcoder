n = int(input())
a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(n)]
#print(a[1][2],b)


tate = []
yoko = []
for i in range(n):
    if "#" in a[i]:
        tate.append(i)
    for j in range(n):
        #print(a[i][j])
        if a[i][j] == "#":
            yoko.append(j)

mintate = min(tate)
maxtate = max(tate)
minyoko = min(yoko)
maxyoko = max(yoko)

crop = []
for i in range(n):
    if i >= mintate and i <= maxtate:
        crop.append(a[i][minyoko:maxyoko+1])
#print(crop)

tate = []
yoko = []
for i in range(n):
    if "#" in b[i]:
        tate.append(i)
    for j in range(n):
        #print(b[i][j])
        if b[i][j] == "#":
            yoko.append(j)

mintate = min(tate)
maxtate = max(tate)
minyoko = min(yoko)
maxyoko = max(yoko)

crop2 = []
for i in range(n):
    if i >= mintate and i <= maxtate:
        crop2.append(b[i][minyoko:maxyoko+1])
#print(crop2)
ans1 = []
ans2 = []
ans3 = []   
#右に九十度
for x in zip(*crop[::-1]):
    ans1.append(list(x))
    #print(*x,sep='')
#左に九十度
tmp = list(zip(*crop))
for x in tmp[::-1]:
    ans2.append(list(x))
    #print(*x,sep='')
#180
for x in crop[::-1]:
    ans3.append(list(x[::-1]))
    #print(*x[::-1],sep='')


if crop2 == crop:
    print("Yes")
elif crop2 == ans1:
    print("Yes")
elif crop2 == ans2:
    print("Yes")
elif crop2 == ans3:
    print("Yes")
else:
    print("No")


