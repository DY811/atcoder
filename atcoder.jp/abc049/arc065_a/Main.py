import re

print ('YES' if re.search(r'\A(dream(er)?|eraser?)+\Z', input()) else 'NO')  