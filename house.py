apple = 5
orange = int(input())
print(apple + orange)



n = int(input())
a = [int(i) for i in input().split()]
sum = 0

for i in range(n):
    sum += a[i]
print(sum)



def trance_binary():
    n = int(input())
    ans = ''
    while n >= 1:
        if n % 2 == 0:
            ans = '0' + ans
        if n % 2 == 1:
            ans = '1' + ans
        n = n // 2
    return ans
print(trance_binary())


a = 2
b = 8
c = 8
print(a * b * c)


import math

print(abs(-12345))
print(11 ** 3)
print(math.sqrt(4))

print(11 & 14)
print(11 | 14)
print(11 ^ 14)
print((11 & 27) & 40)
print((11 | 27) | 40)
print((11 ^ 27) ^ 40)

print(46 << 1)
print(46 >> 3)
print(1 << 31)


n = int(input())
a = [int(x) for x in input().split()]
sum = 0

for i in range(n):
    sum += a[i]

print(sum % 100)


n = int(input())
print((2 * n) + 3)

n, x, y = map(int, input().split())
count = 0
i = 1


while n >= i:
    if i % x == 0 or  i % y == 0:
        count += 1
    i += 1

print(count)