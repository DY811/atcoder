n = int(input())
tango = [] #empty
prefix = []
suffix = []
for i in range(n):
    tango.append(input())
    prefix.append(tango[i][0])
    suffix.append(tango[i][-1])
if len(set(tango)) != n:
    print("No")
    exit()
for i in range(n-1):
    if suffix[i] == prefix[i+1]:
        continue
    if suffix[i] != prefix[i+1]:
        print("No")
        exit()
#print(tango)
#print(prefix)
#print(suffix)
print("Yes")