def solution(sticker):
    answer = [[0, 0], [0, sticker[0]]]
    # 첫 스티커를 땠는지, 이전 스티커를 땠는지...
    for i in range(1, len(sticker) - 1):
        new = [[0, 0], [0, 0]]
        new[0][0] = max(answer[0])
        new[0][1] = answer[0][0] + sticker[i]
        new[1][0] = max(answer[1])
        new[1][1] = answer[1][0] + sticker[i]
        answer = new
    return max(answer[0][0] + sticker[-1], answer[0][1], max(answer[1]))