N = int(input())
A = list(map(int, input().split()))
if N == 1:
    print(A[0])
else:
    A.sort()
    print(max(A[-2], sum(A) / N))