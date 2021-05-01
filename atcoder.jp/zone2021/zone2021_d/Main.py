from collections import deque
s = input()
t = deque()
rev = 0
for i in range(len(s)):
    if s[i] == "R":
        rev += 1
    elif rev%2 == 0:
        t.append(s[i])
        if len(t)>= 2 and t[-1] == t[-2]:
            t.pop()
            t.pop()
    else:
        t.insert(0,s[i])
        if len(t)>= 2 and t[0] == t[1]:
            t.popleft()
            t.popleft()

if rev%2 == 0:
    print("".join(t))
else:
    t.reverse()
    print("".join(t))