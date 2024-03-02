T = int(input())
for _ in range(T):
    N = int(input())
    answer = ''
    for _ in range(N // 2):
        answer += '1'
    if N % 4 == 1:
        answer += '0'
    if N % 4 == 3:
        answer += '2'
    for _ in range(N // 2):
        answer += '1'
    if N == 1:
        answer = '0'
    print(int(answer))