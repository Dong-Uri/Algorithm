def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f(n-1) + f(n-2) + f(n-3)

T = int(input())
for _ in range(T):
    n = int(input())
    print(f(n))