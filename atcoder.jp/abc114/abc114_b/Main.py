s = input()
ans = 999

for i in range(len(s)-2):
    #print(s[i:(i+3)])
    tmp = abs(int(s[i:(i+3)])-753)
    ans = min(ans,tmp)
print(ans)