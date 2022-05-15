import sys
n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
set_l = list(sorted(set(l)))
dic={set_l[i]: i for i in range(len(set_l))}

for i in l:
    print(dic[i], end = ' ')