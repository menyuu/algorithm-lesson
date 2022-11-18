N, n = map(int, input().split())
a = [int(input()) for _ in range(N)]

if n > len(a):
    for i in range(n - len(a)):
        a.append(0)
elif n < len(a):
    del a[n:]

for i in a:
    print(i)


N, n = map(int, input().split())
a = [0] * n

for i in range(N):
    a_i = input()
    if i < n:
        a[i] = a_i

for ele in a:
    print(ele)