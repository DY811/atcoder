#　正の整数の個数
n = int(input())
#　整数のリスト
s = list(map(int,input().split()))

# uniqueな数字とその数を取得
import collections
kumiawase = collections.Counter(s)
#print(kumiawase)

# uniqueな配列の全組み合わせで差の二乗を計算する
import itertools
suuji = kumiawase.keys()
kazu = kumiawase.values()
cnt = 0

for i in itertools.combinations(suuji, 2):
    #print(str(i[0]) + ":" + str(kumiawase[i[0]]), str(i[1]) + ":" + str(kumiawase[i[1]]))
    cnt += kumiawase[i[0]] * kumiawase[i[1]] * (i[0] - i[1])**2
    #print(cnt)
print(cnt)