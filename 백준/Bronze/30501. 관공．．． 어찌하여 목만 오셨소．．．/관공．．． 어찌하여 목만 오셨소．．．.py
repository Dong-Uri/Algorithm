N = int(input())
answer = False
for _ in range(N):
    name = input()
    if name.find('S') != -1:
        answer = name
        break
print(answer)