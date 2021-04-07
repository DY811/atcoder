import math
n = int(input())
x0, y0 = map(int,input().split())
xh, yh = map(int,input().split())
d = math.sqrt((x0-xh)**2+(y0-yh)**2)
#print(d)# 直径
rad = math.radians((180*(n-2))/n)
rad_degree = rad*180/math.pi
#print(rad_degree)
d_next = d*math.sin(math.pi/2-(rad)/2)
#print(d_next)
tilt = math.atan2((yh-y0),(xh-x0)) # 傾き
tilt_degree = tilt*180/math.pi
#print(tilt_degree)
x1 = x0 + d_next*math.cos(tilt-rad/2)
y1 = y0 + d_next*math.sin(tilt-rad/2)
print(x1,y1)

