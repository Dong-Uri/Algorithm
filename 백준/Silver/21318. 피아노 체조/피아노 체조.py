import sys

N = int(sys.stdin.readline().rstrip())
akbo = list(map(int, sys.stdin.readline().rstrip().split()))
miss_list = [0]
miss = 0
for i in range(N - 1):
    if akbo[i] > akbo[i + 1]:
        miss += 1
    miss_list.append(miss)
Q = int(sys.stdin.readline().rstrip())
for _ in range(Q):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(miss_list[y - 1] - miss_list[x - 1])