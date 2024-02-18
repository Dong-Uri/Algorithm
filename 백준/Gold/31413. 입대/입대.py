N, M = map(int, input().split())
s_list = list(map(int, input().split()))
A, D = map(int, input().split())
point = sum(s_list)
if point >= M:
    print(0)
else:
    plus_list = []
    for i in range(N):
        p = sum(s_list[i:min(i + D, N)])
        if p < A:
            plus_list.append(A - p)
        else:
            plus_list.append(0)
    ans_list = [M - point] * (N + 1)
    length = N
    answer = 0
    is_ans = False
    while length > 0:
        answer += 1
        n_ans_list = []
        for i in range(length):
            ans = min(ans_list[min(i + D, N):]) - plus_list[i]
            if ans <= 0:
                is_ans = True
                break
            n_ans_list.append(ans)
        if is_ans:
            break
        length -= D
        ans_list = n_ans_list
    else:
        answer = -1
    print(answer)