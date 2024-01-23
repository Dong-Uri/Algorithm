def solution(my_string, s, e):
    r = my_string[s:e+1]
    answer = my_string[:s] + r[::-1] + my_string[e+1:]
    return answer