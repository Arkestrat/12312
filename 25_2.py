n, k  = int(input()), int(input())
if n == 2:
    x = 0
elif k <= n // 2:
    x = n - 3 - (k - 1)
elif k > n // 2:
    x = n - 3 - (n - k)
print(x)
