def solution(files):
    answer = []
    files_sort = []
    for file in files:
        head = ''
        number = ''
        in_dec = False
        for c in file:
            if c.isdecimal():
                in_dec = True
                number += c
                continue
            else:
                if in_dec:
                    break
                head += c
        files_sort. append([head.lower(), int(number), file])
    files_sort.sort(key=lambda x : x[:2])
    for _, _, file in files_sort:
        answer.append(file)
    return answer