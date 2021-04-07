n, a, b = map(int,input().split())
def digit_sum(x):
  result = 0
  length = len(str(x))
  moji = str(x)
  for i in range(length):
      result += int(moji[i])
  return result
 
ans = 0
for i in range(1,n+1):
    x = digit_sum(i)
    if a <= x <= b:
      ans += i
print(ans)    
        