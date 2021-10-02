s = input()
t = input()

if s == t:
    print("Yes")
    exit
else:
    for i in range(len(s)-1):
        if s[:i]+s[i+1]+s[i]+s[i+2:] == t:
            print("Yes")
            break
    else:
        print("No")