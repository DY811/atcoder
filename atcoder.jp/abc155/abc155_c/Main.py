#import sys
import collections
"""
read = sys.stdin.buffer.read #標準入力から複数行取得するための関数です。 readlines() が結果を行単位で分割してリストで返すのに対して、 read() は結果をそのまま1つの文字列として取得します。
readline = sys.stdin.buffer.readline #標準入力から1行取得するための関数です。
readlines = sys.stdin.buffer.readlines #標準入力から複数行取得するための関数です。戻り値はリストで、入力された文字列が1行ずつ要素として格納されています。
"""

#def solve():
#readline = sys.stdin.buffer.readline
#mod = 10 ** 9 + 7

n = int(input())
s = [input() for _ in range(n)]
#print(s)    
counter = collections.Counter(s)
#print(counter["vet"])
#print(counter.items())
"""
Counterにはmost_common()メソッドがあり、
(要素, 出現回数)という形のタプルを出現回数順に並べたリストを返す。
"""
freq = counter.most_common()
#print(freq)
"""
dictなのでアルファベット順とは限らない

(要素, 出現回数)のタプルではなく、
出現回数順に並べた要素・出現回数のリストが個別に欲しい場合は、
以下のようにして分解できる。
"""
values, counts = zip(*list(counter.most_common()))
max_count = max(counts)
max_values = counts.count(max_count)
ans = list(values[:max_values])
ans.sort()
for i in range(len(ans)):
    print(ans[i])
#s = collections.Counter([str(readline().rstrip().decode('utf-8')) for _ in range(n)]).most_common()
#s.sort(key=lambda x: x[0])
#s.sort(key=lambda x: x[1], reverse=True)
"""
    for k, v in s:
        if v == s[0][1]:
            print(k)
        else:
            break
if __name__ == '__main__':
    solve()
"""