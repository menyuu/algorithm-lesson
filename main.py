n = int(input())
a = [int(input()) for _ in range(n)]

for i in range(n):
    print('i = ',i)
    for j in range(i):
        print('j = ',j)
        print('######################')
        print('a[i] = {}, a[j] = {}'.format(a[i], a[j]))
        print(a[i] * a[j])