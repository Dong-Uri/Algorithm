N = int(input())
coins = [0, 0, 0, 0]
coins[0] = N // 7
N %= 7
coins[1] = N // 5
N %= 5
coins[2] = N // 2
N %= 2
coins[3] = N
while coins[0] and coins[2] and coins[3]:
    coins[1] += 2
    coins[0] -= 1
    coins[2] -= 1
    coins[3] -= 1
print(sum(coins))