h,w,x,y = map(int,input().split())
field = [list(input()) for _ in range(h)]
#print(field[x-1][y-1]) # position
cnt = 0
#left
for i in range(y-1)[::-1]:
    #print(i)
    #print(field[x-1][i])
    if field[x-1][i] == ".":
        cnt += 1
    elif field[x-1][i] == "#":
        break
#print("left"+str(cnt))
#right
for i in range(y,w):
    #print(i)
    if i == w:
        break
    #print(i)
    #print(field[x-1][i])
    if field[x-1][i] == ".":
        cnt += 1
    elif field[x-1][i] == "#":
        break
#print("left+right"+str(cnt))

#upper
for i in range(x-1)[::-1]:
    #print(i)
    #print(field[i][y-1])
    if field[i][y-1] == ".":
        cnt += 1
    elif field[i][y-1] == "#":
        break
#print("leftrightupper"+str(cnt))

#lower
for i in range(x,h):
    if i == h:
        break
    #print(i)
    #print(field[i][y-1])
    if field[i][y-1] == ".":
        cnt += 1
    elif field[i][y-1] == "#":
        break
#print(cnt)

cnt += 1
print(cnt)      