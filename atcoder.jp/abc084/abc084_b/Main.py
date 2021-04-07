#coding: utf-8
import re #regular expression

a,b = map(int,input().split())
s = input()

p_regex = re.compile("\d"*a + "-" + "\d"*b)
if p_regex.search(s):
    print("Yes")
else: 
    print("No")