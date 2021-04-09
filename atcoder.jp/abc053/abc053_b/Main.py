s = input()
r = s[::-1] #reversed
#print(r)
first = s.index("A")
last = r.index("Z")
print(len(s)-first-last)
