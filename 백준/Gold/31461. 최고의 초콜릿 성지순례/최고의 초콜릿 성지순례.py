T = int(input())
for _ in range(T):
    N = int(input())
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    a, b, c, d = map(int, input().split())
    answer = 0
    if b == 1:
        answer += line1[a - 1]
    else:
        answer += line2[a - 1]
    if d == 1:
        answer += line1[c - 1]
    else:
        answer += line2[c - 1]
    if a == c:
        max_point = 0
        sum_point = 0
        for i in range(min(a, c) - 2, -1, -1):
            point = sum_point
            if line1[i] > 0:
                point += line1[i]
            if line2[i] > 0:
                point += line2[i]
            if point > max_point:
                max_point = point
            sum_point += line1[i] + line2[i]
        max_point1 = max_point
        max_point = 0
        sum_point = 0
        for i in range(max(a, c), N):
            point = sum_point
            if line1[i] > 0:
                point += line1[i]
            if line2[i] > 0:
                point += line2[i]
            if point > max_point:
                max_point = point
            sum_point += line1[i] + line2[i]
        max_point2 = max_point
        answer += max(max_point1, max_point2)
    else:
        max_point = 0
        if a < c:
            if b == 1:
                sum_point = line2[a - 1]
                if sum_point > max_point:
                    max_point = sum_point
            else:
                sum_point = line1[a - 1]
                if sum_point > max_point:
                    max_point = sum_point
        else:
            if d == 1:
                sum_point = line2[c - 1]
                if sum_point > max_point:
                    max_point = sum_point
            else:
                sum_point = line1[c - 1]
                if sum_point > max_point:
                    max_point = sum_point
        for i in range(min(a, c) - 2, -1, -1):
            point = sum_point
            if line1[i] > 0:
                point += line1[i]
            if line2[i] > 0:
                point += line2[i]
            if point > max_point:
                max_point = point
            sum_point += line1[i] + line2[i]
        answer += max_point
        max_point = 0
        if a > c:
            if b == 1:
                sum_point = line2[a - 1]
                if sum_point > max_point:
                    max_point = sum_point
            else:
                sum_point = line1[a - 1]
                if sum_point > max_point:
                    max_point = sum_point
        else:
            if d == 1:
                sum_point = line2[c - 1]
                if sum_point > max_point:
                    max_point = sum_point
            else:
                sum_point = line1[c - 1]
                if sum_point > max_point:
                    max_point = sum_point
        for i in range(max(a, c), N):
            point = sum_point
            if line1[i] > 0:
                point += line1[i]
            if line2[i] > 0:
                point += line2[i]
            if point > max_point:
                max_point = point
            sum_point += line1[i] + line2[i]
        answer += max_point
        for i in range(min(a, c), max(a, c) - 1):
            answer += max(line1[i], line2[i])
            if min(line1[i], line2[i]) > 0 :
                answer += min(line1[i], line2[i])
    print(answer)
