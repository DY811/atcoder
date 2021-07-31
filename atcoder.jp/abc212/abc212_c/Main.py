n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

aa = list(set(a))
bb = list(set(b))

#for aaa in aa:
#    if aaa in bb:
#        print(0)
#        exit()
        
if n == 1:
    print(abs(aa[0]-bb[0]))
    exit()

aa.sort()
#print(aa,bb)

def is_closest(n,right, left):
    while right - left > 0:
        #print(right,left)
        mid = (right + left)//2
        if mid == left:
            if abs(aa[mid]-n) < abs(aa[mid+1]-n):
                return aa[mid]
            else:
                return aa[mid+1]
        if aa[mid] >= n:
            right = mid
        else:
            left = mid
    return aa[right]
  
right = len(aa)-1
dif = []
for bi in bb:
    dif.append(abs(is_closest(bi,right,0)-bi))
print(min(dif))





