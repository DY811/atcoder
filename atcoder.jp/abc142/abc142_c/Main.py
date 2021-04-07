n = int(input()) #生徒の人数
a = list(map(int,input().split()))
students = list(range(1,n+1))
#print(students)
dic = {key: val for key, val in zip(a, students)}
#print(dic)
items_sorted = sorted(dic.keys())
#print(items_sorted)
for key in items_sorted:
    print(dic[key], end = ' ')  
  









