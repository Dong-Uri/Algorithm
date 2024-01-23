def solution(k, score):
    answer = []
    hof = [-1] * k
    for n, s in enumerate(score):
        for i in range(k):
            if s > hof[i]:
                for j in range(k-1, i, -1):
                    hof[j] = hof[j-1]                    
                hof[i] = s
                break
        answer.append(hof[min(n, k-1)])
    return answer