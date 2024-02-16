import heapq

def solution(plans):
    answer = []
    working = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x:-x[1])
    while plans:
        plan = plans.pop()
        for work in working:
            if plan[1] < work[2]:
                work[2] += plan[2]
        plan[2] += plan[1]
        working.append(plan)
    working.sort(key=lambda x:x[2])
    for work in working:
        answer.append(work[0])
    return answer