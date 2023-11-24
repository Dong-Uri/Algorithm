def solution(money):
    answer = [[0, 0], [0, money[0]]]
    # 첫 집을 털었는지, 이전 집을 털었는지...
    for i in range(1, len(money) - 1):
        new = [[0, 0], [0, 0]]
        new[0][0] = max(answer[0])
        new[0][1] = answer[0][0] + money[i]
        new[1][0] = max(answer[1])
        new[1][1] = answer[1][0] + money[i]
        answer = new
    return max(answer[0][0] + money[-1], answer[0][1], max(answer[1]))