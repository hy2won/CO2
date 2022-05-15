n = int(input())
l = []

for _ in range(n):
    a = list(input().split())
    l.append(a)
    
l.sort(key=lambda x:int(x[0]))

for i in l:
    print(i[0], i[1])

