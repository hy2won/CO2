import sys

n = int(input())

l = []
for _ in range(n):
    l.append(input())
    
set_l = set(l)
l = list(set_l)
l.sort()
l.sort(key = len)

for i in l:
    print(i)
