import copy
def solution(n, info):
    def shot(ryan_shot, ryan, apeach, n, info, i):
        nonlocal ans
        nonlocal chai
        if ryan > apeach and n >= 0:
            ans_ryan_shot = copy.deepcopy(ryan_shot)
            ans_ryan_shot[-1] += n
            if ryan - apeach > chai:
                ans = ans_ryan_shot
                chai = ryan - apeach
            elif ryan - apeach == chai:
                for j in range(10, -1, -1):
                    if ans_ryan_shot[j] > ans[j]:
                        ans = ans_ryan_shot
                        chai = ryan - apeach
                        break
                    elif ans_ryan_shot[j] < ans[j]:
                        break
        if i < 11 and n > 0:
            shot(ryan_shot, ryan, apeach, n, info, i + 1)
            ryan_shot_ = copy.deepcopy(ryan_shot)
            ryan_shot_[i] = info[i] + 1
            if info[i]:
                apeach -= 10 - i
            shot(ryan_shot_, ryan + 10 - i, apeach, n - info[i] - 1, info, i + 1)
    apeach = 0
    for i, a in enumerate(info):
        if a:
            apeach += 10 - i
    ryan = 0
    ryan_shot = [0,0,0,0,0,0,0,0,0,0,0]
    ans = [0,0,0,0,0,0,0,0,0,0,0]
    chai = 0
    shot(ryan_shot, ryan, apeach, n, info, 0)
    if ans == [0,0,0,0,0,0,0,0,0,0,0]:
        return [-1]
    else:
        return ans