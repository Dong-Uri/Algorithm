def solution(edges, target):
    answer = []
    nodes = [[[], 0] for _ in range(len(target))]
    for edge in edges:
        nodes[edge[0] - 1][0].append(edge[1] - 1)
    for node in nodes:
        node[0].sort()
    TF = [False] * len(target)
    for i in range(len(target)):
        if not target[i]:
            TF[i] = True
    goal = []
    nums = [0] * (len(target))
    while True:
        i = 0
        while True:
            if not nodes[i][0]:
                break
            new_i = nodes[i][0][nodes[i][1]]
            nodes[i][1] += 1
            if nodes[i][1] == len(nodes[i][0]):
                nodes[i][1] = 0
            i = new_i
        goal.append(i)
        nums[i] += 1
        if not TF[i] and target[i] >= nums[i] and target[i] <= 3 * nums[i]:
            TF[i] = True
        elif TF[i] and target[i] < nums[i]:
            return [-1]
        if all(TF):
            break
    for i in range(len(nums)):
        target[i] -= nums[i]
        nums[i] = [1] * nums[i]
        j = -1
        while target[i]:
            if target[i] >= 2:
                nums[i][j] += 2
                target[i] -= 2
                j -= 1
            else:
                nums[i][j] += 1
                target[i] -= 1
    for g in goal:
        answer.append(nums[g].pop(0))
    return answer