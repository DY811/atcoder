s = input()
s = list(s[::-1]) # 後ろから
s[0:5]  
# print("".join(s[0:2]))
# print(s.pop(0))
# pop_list = range(0,5)
#print(s)
while len(s) >=5:
    if "".join(s[0:5]) == "maerd":
        #先頭の5文字を除く
        pop_list = range(0,5)
        for i in sorted(pop_list, reverse=True):
            s.pop(i) 
    elif "".join(s[0:7]) == "remaerd":
        #先頭の7文字を除く
        pop_list = range(0,7)
        for i in sorted(pop_list, reverse=True):
            s.pop(i)
    elif "".join(s[0:5]) == "esare":
        #先頭の5文字を除く
        pop_list = range(0,5)
        for i in sorted(pop_list, reverse=True):
            s.pop(i)
    elif "".join(s[0:6]) == "resare":
        #先頭の7文字を除く
        pop_list = range(0,6)
        for i in sorted(pop_list, reverse=True):
            s.pop(i)
    else:         
        break
        
if len(s) == 0: #うまくいった時           
    print("YES")
elif len(s) >= 5: #↑でbreakした時
    print("NO")
else: #文字が余る時
    print("NO")     