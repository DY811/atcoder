import re
S = input()
is_match = re.compile(r"A[a-z]+C[a-z]+$")
if is_match.search(S):
    print("AC")
else:
    print("WA")