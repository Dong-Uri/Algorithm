def solution(n):
    answer = [0, 1, 2]
    while len(answer) <= n:
        answer.append((answer[-1] + answer[-2]) % 1000000007)
    return answer[n]