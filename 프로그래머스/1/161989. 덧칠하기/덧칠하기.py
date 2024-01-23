def solution(n, m, section):
    answer = 0
    if not section:
        return 0
    paint_start = section.pop()
    answer += 1
    while section:
        painting = section.pop()
        if painting <= paint_start - m:
            paint_start = painting
            answer += 1
    return answer