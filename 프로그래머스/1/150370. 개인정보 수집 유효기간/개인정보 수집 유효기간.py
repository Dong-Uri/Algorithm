def solution(today, terms, privacies):
    answer = []
    y, m, d = map(int, today.split('.'))
    term_limit = {}
    for term in terms:
        yy = y
        mm = m
        policy, month = term.split()
        mm -= int(month)
        while mm <= 0:
            mm += 12
            yy -= 1
        term_limit[policy] = [yy, mm, d]
    
    for i, privacy in enumerate(privacies):
        date, policy = privacy.split()
        y, m, d = map(int, date.split('.'))
        if y < term_limit[policy][0]:
            answer.append(i + 1)
        elif y > term_limit[policy][0]:
            continue
        elif m < term_limit[policy][1]:
            answer.append(i + 1)
        elif m > term_limit[policy][1]:
            continue
        elif d <= term_limit[policy][2]:
            answer.append(i + 1)
            
    return answer