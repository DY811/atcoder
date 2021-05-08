d,n = map(int,input().split())
cnt = 0
num = 1
def divide(x):
    cnt = 0
    while x%100 == 0:
        cnt += 1
        x = x//100
    return cnt

while cnt < n:
    if num % 100 != 0:
        #print("a")
        if d == 0:
            #print("b")
            cnt += 1
            num += 1
        else:
            num += 1
    else:
        if divide(num) == d:
            #print(num)
            cnt += 1
            num += 1
        else:
            num += 1
print(num-1)