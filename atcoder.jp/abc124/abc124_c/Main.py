s = input()
if len(s) == 1:
    print(0)
elif len(s) % 2 == 0: #even
    l = len(s)/2
    black = "10"*int(l)
    white = "01"*int(l)
    b_c = 0
    w_c = 0
    for i in range(len(s)):
        if s[i] == black[i]:
            b_c += 1
        else:
            w_c += 1
    common = max(b_c,w_c)
    print(len(s)-common)
elif len(s) % 2 != 0: #odd
    l = len(s)/2
    black = "10"*int(l)+"1"
    white = "01"*int(l)+"0"
    b_c = 0
    w_c = 0
    for i in range(len(s)):
        if s[i] == black[i]:
            b_c += 1
        else:
            w_c += 1
    common = max(b_c,w_c)
    print(len(s)-common)