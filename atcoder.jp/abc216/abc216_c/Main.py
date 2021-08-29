import sys
sys.setrecursionlimit(1000000)
n = int(input())

s = ""
temp = n
for i in range(120):
    if temp%2==0:
        cnt=0
        while temp%2==0:
            cnt+=1
            temp //= 2
        #print(temp,cnt)
        s = s+"B"*cnt
        #print(cnt,temp)
    elif temp == 1:
        s = s+"A"
        break
    else:
        temp -= 1
        s = s+"A"
print(s[::-1])


