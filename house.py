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