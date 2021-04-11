from itertools import groupby
n = input()
r = n[::-1]
#print(n,r)
dst = [sum(1 for e in it) for _, it in groupby(r, key=lambda x: x == "0")]
#print(dst)
if r[0]=="0":
    zero_count = dst[0]
    add = r+"0"*zero_count
    add_reverse = add[::-1]
    #print(add)
    if add == add_reverse:
        print("Yes")
    else:
        print("No")
else: #no zero
    if n == r:
        print("Yes")
    else:
        print("No")
  