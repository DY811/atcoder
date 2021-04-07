ss = input()
ss = list(ss[::-1])
n = len(ss)
lower_s = ""
upper_s = ""
#print(n)
while len(ss)>1:
    #print(ss)
    lower_s += ss.pop()
    upper_s += ss.pop()
if len(ss)==1:
    lower_s += ss.pop()
#print(lower_s)
#print(upper_s)

if n == 1 and str(lower_s).islower() == True:
    print("Yes")
elif str(lower_s).islower() == True and str(upper_s).isupper() == True:
    print("Yes")
else:
    print("No")