n = int(input())
s = input()
x = 0
ans = 0

for i in s:
    #print(i,ans)
    if i == "I":
        x += 1
        ans = max(ans,x)
    elif i == "D":
        x -= 1
print(ans)