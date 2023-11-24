def solution(n, s, a, b, fares):
    S = [20000000] * (n+1)
    A = [20000000] * (n+1)
    B = [20000000] * (n+1)
    ways = [[] for _ in range(n+1)]
    for fare in fares:
        ways[fare[0]].append([fare[1], fare[2]])
        ways[fare[1]].append([fare[0], fare[2]])
    stk = [s]
    S[s] = 0
    while stk:
        now = stk.pop()
        for way in ways[now]:
            if S[now] + way[1] < S[way[0]]:
                S[way[0]] = S[now] + way[1]
                if way[0] not in stk:
                    stk.append(way[0])
    stk = [a]
    A[a] = 0
    while stk:
        now = stk.pop()
        for way in ways[now]:
            if A[now] + way[1] < A[way[0]]:
                A[way[0]] = A[now] + way[1]
                if way[0] not in stk:
                    stk.append(way[0])
    stk = [b]
    B[b] = 0
    while stk:
        now = stk.pop()
        for way in ways[now]:
            if B[now] + way[1] < B[way[0]]:
                B[way[0]] = B[now] + way[1]
                if way[0] not in stk:
                    stk.append(way[0])
    answer = 60000000
    for i in range(1, n+1):
        if S[i] + A[i] + B[i] < answer:
            answer = S[i] + A[i] + B[i]
    return answer