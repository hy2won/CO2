n = int(input())
l = []
for _ in range(n):
    a = list(map(int,input().split()))
    l.append(a)

l.sort()
for i in l:
    print(i[0],i[1])