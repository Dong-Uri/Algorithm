def solution(survey, choices):
    score = {'RT': 0, 'CF': 0, 'JM': 0, 'AN': 0}
    for i in range(len(survey)):
        if survey[i] in score.keys():
            score[survey[i]] += choices[i] - 4
        else:
            score[survey[i][::-1]] += 4 - choices[i]
    answer = ''
    for t, s in score.items():
        if s <= 0:
            answer += t[0]
        else:
            answer += t[1]
    return answer