x = input()
if x.count(".")>=1:
    end = x.find(".")
    print(x[0:end])
else:
    print(x)