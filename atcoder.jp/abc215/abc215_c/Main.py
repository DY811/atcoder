from itertools import permutations

s,k = map(str,input().split())
s = list(s)
k = int(k)

st = list(permutations(s))
#for i in range(s)

st = list(set(st))
st.sort()
ans = st[k-1]
print(''.join(str(x) for x in ans))