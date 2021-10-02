n = list(input())
#print(n)
ans = 0
for i in range(2**len(n)):
    a = ""
    b = ""
    for j in range(len(n)):
        if ((i >> j)&1):
            a += n[j]
            #print(a)
        else:
            b += n[j]
            #print(b)
    #print(a,b)
    if len(a) == 0 or len(b) == 0:
        continue
    elif a[0] == "0" or b[0] == "0":
        continue
    else:
        aa = list(a)
        bb = list(b)
        aa.sort(reverse = True)
        bb.sort(reverse = True)
        aa = "".join(aa)
        bb = "".join(bb)
        #print(str(aa),str(bb),int(aa)*int(bb))
        ans = max(ans,int(aa)*int(bb))
print(ans)