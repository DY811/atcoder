# Panasonic Programming Contest B Bishop
H, W = list(map(int, input().split()))
if H % 2 != 0:
    odd_row = H // 2 +1
else: 
    odd_row = H // 2
even_row = H // 2

if W % 2 != 0:
    odd_panel = W // 2 + 1
else:
    odd_panel = W // 2
even_panel = W // 2
cnt = odd_row*odd_panel + even_row*even_panel
#print(odd_row,odd_panel,even_row,even_panel)
if H == 1 or W == 1: # cannot move
    print(1)
else:
    print(cnt)