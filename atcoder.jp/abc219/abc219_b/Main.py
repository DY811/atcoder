s1 = input()
s2 = input()
s3 = input()
t = input()
ans = ''
for i in range(len(t)):
    if t[i] == '1':
        ans += s1
    elif t[i] == '2':
        ans += s2
    elif t[i] == '3':
        ans += s3
print(ans)