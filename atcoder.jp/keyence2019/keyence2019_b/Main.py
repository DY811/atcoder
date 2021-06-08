import re
s = input()
text = '(.*)'
key = 'keyence'
candidates = [key]*(len(key)+1)
for i in range(len(key)+1):
    candidates[i] = '\A'+candidates[i][:i]+text+candidates[i][i:]+'\Z'
#print(candidates)

ans = False
for i in range(len(key)+1):
    if re.search(candidates[i],s):
        ans = True
        print('YES')
        break
else:
    print('NO')