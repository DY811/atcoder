from collections import *

n = int(input())
blue = []
for i in range(n):
    blue.append(input())
    
m = int(input())
red = []
for i in range(m):
    red.append(input())

blue_list = Counter(blue)
red_list = Counter(red)
#most_common()で多い順
#print(blue_list.most_common()[0])
#最も少ないものは−1
#print(blue_list.most_common()[-1])
b_values, b_counts = zip(*blue_list.most_common())
r_values, r_counts = zip(*red_list.most_common())

score = 0 #どこにもかいてないものを言えばゼロ
for i in range(len(b_values)):
    v = b_values[i]
    if  v in b_values and v in r_values:
        tmp = b_counts[b_values.index(v)] - r_counts[r_values.index(v)]
    elif v in b_values:
        tmp = b_counts[b_values.index(v)]
    else :
        continue
    score = max(score, tmp)
print(score)