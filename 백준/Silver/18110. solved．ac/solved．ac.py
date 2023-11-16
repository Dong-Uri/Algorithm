import sys

n = int(sys.stdin.readline().rstrip())
if not n:
    print(0)
else:
    lst = []
    for _ in range(n):
        lst.append(int(sys.stdin.readline().rstrip()))
    lst.sort()
    a = n * 15 / 100
    x = int(a)
    b = a - x
    if b >= 0.5:
        x += 1
    a = sum(lst[x:len(lst) - x]) / (len(lst) - 2 * x)
    y = int(a)
    b = a - y
    if b >= 0.5:
        y += 1
    print(y)