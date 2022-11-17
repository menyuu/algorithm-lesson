apple = 5
orange = int(input())
print(apple + orange)


n = int(input())
a = [int(i) for i in input().split()]
sum = 0

for i in range(n):
    sum += a[i]
print(sum)