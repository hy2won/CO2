n = int(input())

list = []
for i in str(n):
    list.append(i)

list.sort(reverse = True)

print(''.join(map(str,list)))