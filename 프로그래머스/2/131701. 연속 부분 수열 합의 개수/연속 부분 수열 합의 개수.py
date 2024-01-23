def solution(elements):
    ans_set = set(elements)
    ans_set.add(sum(elements))
    for i in range(2, len(elements)):
        for j in range(len(elements)):
            if j+i < len(elements):
                ans_set.add(sum(elements[j:j+i]))
            else:
                ans_set.add(sum(elements[j:]+elements[:j+i-len(elements)]))
    answer = len(ans_set)
    return answer