N = int(input())
n = list(range(1,N+1))
#print(n)
P = list(map(str,input().split()))
Q = list(map(str,input().split()))
p = int(''.join(P)) #joinで文字列を繋げて数字に変換する
q = int(''.join(Q))
#print(p,q)

import itertools
all_list = list(itertools.permutations(n,N)) #from smallest to largest
#print(all_list)

num_list = [] # empty (len=0) 
for i in all_list:
  #print(''.join(map(str,i)))
  num_list.append(''.join(map(str,i)))

#print(num_list)
num_list = list(map(int,num_list))
p_rank = num_list.index(p)+1
q_rank = num_list.index(q)+1
print(abs(p_rank-q_rank))