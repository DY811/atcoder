xy = input()

if int(xy[-1]) >= 0 and int(xy[-1]) <= 2:
    print(xy[:-2]+"-")
elif int(xy[-1]) >= 3 and int(xy[-1]) <= 6:   
    print(xy[:-2])
else:
    print(xy[:-2]+"+")


