n = int(input())
a = [int(input()) for _ in range(n)]

for i in range(n):
    print('i = ',i)
    for j in range(i):
        print('j = ',j)
        print('######################')
        print('a[i] = {}, a[j] = {}'.format(a[i], a[j]))
        print(a[i] * a[j])

#########################################################

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


n = int(input())
a = [int(input()) for _ in range(n)]
x = sorted(set(a), key=a.index)

for i in x:
    print(i)

#########################################################

n = int(input())
m = [int(i) for i in input().split()]
r = []
max = 0

for i in range(n):
    x = [int(x) for x in input().split()]
    sum = 0
    for j in range(len(x)):
        sum += (x[j] * m[j])
    r.append(sum)

for i in r:
    if max <= i:
        max = i

print(max)

n = int(input())
m = list(map(int,input().split()))
ans = 0

for i in range(n):
    a = list(map(int, input().split()))
    score = 0
    for j in range(5):
        score += a[j] * m[j]
    if score > ans:
        ans = score

print(ans)


#########################################################


n = int(input())
a = [int(input()) for _ in range(n)]
min = 200
b = []

for i in range(n):
    for j in range(i):
        if a[j] >= a[i]:
            x = a[j] - a[i]
            if min >= x:
                min = x
                b.clear()
                b.append(a[i])
                b.append(a[j])
        else:
            y = a[i] - a[j]
            if min >= y:
                min = y
                b.clear()
                b.append(a[j])
                b.append(a[i])

n = int(input())
a = [int(input()) for _ in range(n)]
ans = [None, None]
diff = 101

for i in range(n):
    for j in range(i + 1, n):
        if abs(a[i] - a[j]) < diff:
            diff = abs(a[i] - a[j])
            ans = [a[i], a[j]]

ans.sort()
for i in ans:
    print(i)


#########################################################


p = []
ans_p = 0
ans_num = 0

for i in range(4):
    p += input().split()
    print(p)

for i in range(10):
    if p[i] == "1":
        ans_num += 1
        ans_p = 10 - i

print(ans_p)
print(ans_num)
