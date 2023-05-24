N = int(input())
file_name = input()
l = len(file_name)
state = [True] * l
for _ in range(N-1):
    new_name = input()
    for i in range(l):
        if state[i] and file_name[i] != new_name[i]:
            state[i] = False
for i in range(l):
    if state[i]:
        print(file_name[i], end='')
    else:
        print('?', end='')