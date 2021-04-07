a, b, w = map(float, input().split())
max = int(w*1000 // a)
min = int(w*1000 // b)
ans_min = 0
ans_max = 0
#print(min)
#print(max)

# for i in range(int(min),int(max+1)):
#    print(i)


for i in range(min, max+1):
    #print(i)
    if w*1000/i >= a and w*1000/i <= b:
        ans_min = i
        break
for i in range(max, min-1, -1):
    #print(i)
    if w*1000/i >= a and w*1000/i <= b:
        ans_max = i
        break
if ans_min == 0 and ans_max == 0:
    print("UNSATISFIABLE")
else:
    print(ans_min,ans_max) 