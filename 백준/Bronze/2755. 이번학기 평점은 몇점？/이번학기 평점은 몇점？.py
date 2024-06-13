N = int(input())
score_dict = {'A+':4.3, 'A0':4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F':0.0}
point_sum = 0
score_sum = 0
for _ in range(N):
    _, point, score = input().split()
    point = int(point)
    score = score_dict[score]
    point_sum += point
    score_sum += point * score
ans = score_sum / point_sum + 0.000000000000001
print(f'{ans:.2f}')