def solution(users, emoticons):
    def discount(i, spends):
        nonlocal answer
        if i == len(emoticons):
            plus = 0
            earn = 0
            for j in range(len(users)):
                if spends[j] >= users[j][1]:
                    plus += 1
                else:
                    earn += spends[j]
            if plus > answer[0] or (plus == answer[0] and earn > answer[1]):
                answer = [plus, earn]
            return
        spends_10 = spends[:]
        spends_20 = spends[:]
        spends_30 = spends[:]
        spends_40 = spends[:]
        price = emoticons[i] * 0.9
        for j in range(len(users)):
            if users[j][0] <= 10:
                spends_10[j] += price
        price = emoticons[i] * 0.8
        for j in range(len(users)):
            if users[j][0] <= 20:
                spends_20[j] += price
        price = emoticons[i] * 0.7
        for j in range(len(users)):
            if users[j][0] <= 30:
                spends_30[j] += price
        price = emoticons[i] * 0.6
        for j in range(len(users)):
            if users[j][0] <= 40:
                spends_40[j] += price
        discount(i + 1, spends_10)
        discount(i + 1, spends_20)
        discount(i + 1, spends_30)
        discount(i + 1, spends_40)
        return
    answer = [0, 0]
    spends = [0] * len(users)
    discount(0, spends)
    return answer