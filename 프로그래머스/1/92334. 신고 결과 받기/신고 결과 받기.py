def solution(id_list, report, k):
    singo_dct = {}
    for name in id_list:
        singo_dct[name] = [0, []]
    for r in report:
        a, b = r.split()
        if b not in singo_dct[a][1]:
            singo_dct[a][1].append(b)
            singo_dct[b][0] += 1
    answer = []
    for name in id_list:
        mail = 0
        for singo in singo_dct[name][1]:
            if singo_dct[singo][0] >= k:
                mail += 1
        answer.append(mail)
    return answer