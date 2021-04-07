s = int(input()) # first num
ans = [s]
ai = s
for i in range(2,1000000+1):
    #print(i)
    ai_1 = ai
    if ai % 2 == 0: #even
        ai  = ai_1/2
    else: #odd
        ai = 3*ai_1 + 1
    if ai in ans:
        print(i)
        break
    else:
        ans.append(ai)