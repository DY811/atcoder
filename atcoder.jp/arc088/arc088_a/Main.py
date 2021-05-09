x,y = map(int,input().split())
cnt = 0
num = x
while num <= y:
    #print(num)
    num = 2*num
    cnt += 1
print(cnt)