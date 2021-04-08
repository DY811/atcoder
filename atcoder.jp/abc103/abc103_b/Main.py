# 入力
S=input()
T=input()

for i in range(len(S)):
  # 回転
  S=S[-1]+S[:-1]

  # 一致する場合
  if S==T:
    print('Yes')
    exit()

# 最後まで一致しなければ'No'
print('No')