import math

N, S = map(int, input().split())
y_lst = list(map(int, input().split()))
y_lst.append(S)
y_lst.sort()
far_lst = []
for i in range(N):
    far_lst.append(y_lst[i+1] - y_lst[i])
ans = far_lst[0]
for far in far_lst[1:]:
    ans = math.gcd(ans, far)
print(ans)