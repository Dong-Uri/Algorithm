N = int(input())
answer = 0
a_list = list(map(int, input().split()))
for i, a in enumerate(a_list):
    if a == i + 1:
        a_list[i] = i
        if i == 0:
            a_list[i] = N
        answer += 1
print(answer)
print(*a_list)