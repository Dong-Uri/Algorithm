def solution(video_len, pos, op_start, op_end, commands):
    def total_seconds(t):
        mm, ss = map(int, t.split(':'))
        return mm * 60 + ss
    video_len = total_seconds(video_len)
    pos = total_seconds(pos)
    op_start = total_seconds(op_start)
    op_end = total_seconds(op_end)
    for cmd in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if cmd == 'next':
            pos += 10
            if pos > video_len:
                pos = video_len
        if cmd == 'prev':
            pos -= 10
            if pos < 0:
                pos = 0
    if op_start <= pos <= op_end:
        pos = op_end
    answer = ''
    mm = pos // 60
    ss = pos % 60
    if mm < 10:
        answer += '0'
    answer += str(mm)
    answer += ':'
    if ss < 10:
        answer += '0'
    answer += str(ss)
    return answer