import  bisect
n,m,x = map(int,input().split()) # ますの数−1、料金所の数、最初の位置
a = list(map(int,input().split())) # tollgates
#print(a)
index = bisect.bisect_left(a,x)
#print(index)
toll_0 = index 
toll_n = len(a) - index
print(min(toll_0,toll_n))
