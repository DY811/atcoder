s = input()
s_list = list(s)
len_s = len(s)
set_s = len(set(s_list))#unique

if len_s == set_s:
    print("yes")
else: print("no")