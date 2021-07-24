from collections import Counter, defaultdict

MOD = 10**9 + 7
s = input()
word = "chokudai"

ans = 0
ways = defaultdict(int)
##https://kyam-013.hatenablog.jp/entry/2017/07/21/021106

for c in s:
    if c in word:
        i = word.index(c)
        #print(i)
        if i > 0:
            #2文字目以降の場合は前の文字までの通り数分ある条件を加える
            ways[c] += ways[word[i - 1]]
        else:
            ways[c] += 1
        ways[c] %= MOD
#print(ways)
print(ways["i"])


