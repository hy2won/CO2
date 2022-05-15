n = int(input())
l = []
for _ in range(n):
    a = list(map(int,input().split()))
    l.append(a)

l.sort(key=lambda x:(x[1],x[0]))
for i in l:
    print(i[0],i[1])

