a,b = map(int,input().split())

if a <= 0 and b >= 0: # include zero
    print("Zero")
elif a >= 0: # all components are positive
    print("Positive")
elif a <= 0 and b < 0: # all components are negative
    if abs(a-b)%2 == 0: # odd components
        print("Negative")
    else:
        print("Positive")