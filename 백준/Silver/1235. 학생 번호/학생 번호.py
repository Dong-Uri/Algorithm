N = int(input())
stu_num = input()
n = len(stu_num)
set_list = [set() for _ in range(n - 1)]
for i in range(1, n):
    set_list[i - 1].add(stu_num[-i:])
for _ in range(N - 1):
    stu_num = input()
    for i in range(1, n):
        set_list[i - 1].add(stu_num[-i:])
for i in range(1, n):
    if len(set_list[i - 1]) == N:
        print(i)
        break
else:
    print(n)