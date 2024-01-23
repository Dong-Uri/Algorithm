def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))
    Ss = [0] * (row_end - row_begin + 1)
    for i in range(row_begin, row_end+1):
        for n in data[i-1]:
            Ss[i-row_begin] += n % i
    answer = 0
    n = 1
    while sum(Ss):
        xor = False
        for i in range(len(Ss)):
            if Ss[i] % 2:
                if xor:
                    xor = False
                else:
                    xor = True
            Ss[i] //= 2
        if xor:
            answer += n
        n *= 2
    return answer