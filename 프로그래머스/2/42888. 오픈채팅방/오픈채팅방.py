def solution(record):
    nick_dict = {}
    log_list = []
    for r in record:
        r_list = r.split()
        if r_list[0] == 'Enter':
            nick_dict[r_list[1]] = r_list[2]
            log_list.append([r_list[1], '님이 들어왔습니다.'])
        elif r_list[0] == 'Leave':
            log_list.append([r_list[1], '님이 나갔습니다.'])
        else:
            nick_dict[r_list[1]] = r_list[2]
    answer = []
    for log in log_list:
        answer.append(nick_dict[log[0]] + log[1])
    return answer