s = input()
maxs = s
mins = s
    
news = s[1:]+s[0]
    
for i in range(len(s)):
    news = news[1:]+news[0]
    maxs = max(maxs,news)
    mins = min(mins,news)
print(mins)
print(maxs)