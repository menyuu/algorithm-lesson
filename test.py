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


#########################################################

n, q = map(int, input().split())
students = list(range(1, n + 1))

for _ in range(q):
    s = input().split()
    if s[0] == "swap":
        a = int(s[1]) - 1
        b = int(s[2]) - 1
        tmp = students[a]
        students[a] = students[b]
        students[b] = tmp
    elif s[0] == "reverse":
        students.reverse()
    else:
        c = int(s[1])
        if len(students) > c:
            students = students[:c]

for student in students:
    print(student)

n, q = map(int, input().split())
s = [i for i in range(1, n + 1)]

for _ in range(q):
    x = input().split()
    if x[0] == 'swap':
        a = int(x[1]) - 1
        b = int(x[2]) - 1
        tmp = x[a]
        x[a] = x[b]
        x[b] = tmp
    elif x[0] == 'reverse':
        s.reverse()
    else:
        n = int(x[1])
        if len(s) > n:
            del s[n:]

for j in s:
    print(j)


#########################################################


N, K = map(int, input().split())
roster = {x: y for x, y in [input().split() for _ in range(N)]}

for _ in range(K):
    s = input().split()
    if s[0] == "join":
        num, ID = s[1:]
        roster[num] = ID
    elif s[0] == "leave":
        num = s[1]
        del roster[num]
    else:
        num = s[1]
        print(roster[num])


#########################################################

n, k = map(int, input().split())
s = [input() for i in range(n)]
d = {}

for _ in range(k):
    y, c = input().split()
    y = int(y)
    d[y] = c

for y, c in sorted(d.items()):
    print(c)


n, k = map(int, input().split())
s = [input() for i in range(n)]

l = [None] * k
for i in range(k):
    y, c = input().split()
    l[i] = (int(y), c)

for y, c in sorted(l):
    print(c)


#########################################################


n, k = map(int, input().split())
d = {}

for _ in range(n):
    a, b, c = input().split()
    d[a] = (b, int(c))

for _ in range(k):
    x, y, z = input().split()
    a, b = d[x]
    if a != y:
        continue
    d[x] = (a, b - int(z))

for i, j in d.items():
    print(i, d[i][1])


#########################################################


v = input().split()
N = int(v[0])
K = float(v[1])

total = 0
for _ in range(N):
    x = float(input())
    total += round(x * 10)

ans = int(total / round(K * 10))
if total % round(K * 10) != 0:
    ans += 1
print(ans)