n = int(input())
card = map(int,input().split())
sort_card = sorted(card,reverse=True)
# https://note.nkmk.me/python-collections-deque/
from collections import deque
sort_card = deque(sort_card)
alice_point = 0
bob_point = 0
if len(sort_card) % 2 == 0:
    last = 'bob'
else: last = 'alice'

alice_point += sort_card.popleft()
while len(sort_card) >= 2:
    bob_point += sort_card.popleft()
    alice_point += sort_card.popleft()

if last == 'bob': #len(sort_card) = 1
    bob_point += sort_card.popleft()
    
print(alice_point - bob_point)