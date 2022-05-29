n = int(input())
result = 0
for i in range(n):
    array = list(map(int, str(i)))
    s = i + sum(array)
    if s == n:
        print(i)
        break
else:
    print(0)
