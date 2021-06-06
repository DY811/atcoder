# おまじない
import sys
sys.setrecursionlimit(10000)

# 入力の読み込み
N,M=map(int,input().split())
G=[[] for i in range(N)]
# G[i] は都市iから道路で直接繋がっている都市のリスト
for i in range(M):
  A,B=map(int,input().split())
  G[A-1].append(B-1)

# dfs
def dfs(v):
  if temp[v]: return  # 同じ頂点を2度以上調べないためのreturn
  temp[v]=True
  for vv in G[v]: dfs(vv)

ans=0

# 都市iからスタートする場合
for i in range(N):
	temp=[False]*N
	# temp[j] は都市jに到達可能かどうかを表す
	dfs(i)
	ans+=sum(temp)

print(ans)

