def solution(points, routes):
    def moving_route(route):
        mr = [points[route[0] - 1]]
        route.pop(0)
        while route:
            if mr[-1] == points[route[0] - 1]:
                route.pop(0)
            elif mr[-1][0] > points[route[0] - 1][0]:
                mr.append([mr[-1][0] - 1, mr[-1][1]])
            elif mr[-1][0] < points[route[0] - 1][0]:
                mr.append([mr[-1][0] + 1, mr[-1][1]])
            elif mr[-1][1] > points[route[0] - 1][1]:
                mr.append([mr[-1][0], mr[-1][1] - 1])
            else:
                mr.append([mr[-1][0], mr[-1][1] + 1])
        return mr
    mrs = []
    for route in routes:
        mrs.append(moving_route(route))
    answer = 0
    i = 0
    while True:
        cnt_dict = {-1:0}
        for mr in mrs:
            if i < len(mr):
                now = (mr[i][0] - 1) * 100 + mr[i][1] - 1
                if now in cnt_dict.keys():
                    if cnt_dict[now] == 1:
                        answer += 1
                    cnt_dict[now] += 1
                else:
                    cnt_dict[now] = 1
                cnt_dict[-1] += 1 
        if cnt_dict[-1] <= 1:
            break
        i += 1
    return answer