s = input()
k = int(input())
num = []
first = len(s)+1
for i in range(len(s)):
    if int(s[i]) == 1:
        continue
    else:
        first = min(first,i)
        num.append(int(s[i]))
#print(num)
if len(num) == 0 or first >= k:
    print(1)
else:
    print(num[0])