import sys
from collections import Counter

n = int(sys.stdin.readline())
list = []
for _ in range(n):
    list.append(int(sys.stdin.readline()))

print(round(sum(list)/n))

list.sort()
print(list[n//2])

cnt_list = Counter(list).most_common()
if len(cnt_list) > 1 and cnt_list[0][1] == cnt_list[1][1]:
    print(cnt_list[1][0])
else:
    print(cnt_list[0][0])

print(list[-1] - list[0])
