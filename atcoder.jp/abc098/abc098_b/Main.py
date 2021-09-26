n = int(input())
s = input()
ans = 0
for i in range(1,n):
    str1 = set([x for x in s[:i]])
    str2 = set([x for x in s[i:]])
    cnt = len(str1&str2)
    ans = max(ans,cnt)
print(ans)