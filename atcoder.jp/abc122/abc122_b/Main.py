s = input()
#print(s[0])
s = s.replace('A','*')
s = s.replace("C","*")
s = s.replace("G","*")
s = s.replace("T","*")
#print(s)
#s = list(s)
#print(s)
for i in range(1,len(s)+1)[::-1]:
    #print(i)
    case = "*"*i
    if case in s:
        print(i)
        break
else:
    print(0)