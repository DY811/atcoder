menu = [int(input()) for i in range(5)]
t = []
for i in menu:
  t.append((10-i%10)%10) #additional waiting time (2回あるのはmax123minだから)
print(sum(menu)+sum(t)-max(t))