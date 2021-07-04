s = input()

for i in range(1,len(s)):
    tmp = s[:-i]
    #print(tmp)
    if tmp[:len(tmp)//2] == tmp[len(tmp)//2:]:
        print(len(tmp[:len(tmp)//2])*2)
        break