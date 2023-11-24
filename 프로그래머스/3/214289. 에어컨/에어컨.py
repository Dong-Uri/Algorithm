def solution(temperature, t1, t2, a, b, onboard):
    safe = t2 - t1 + 1
    if temperature > t2:
        out = temperature - t2
    else:
        out = t1 - temperature
    stat = [100000] * (safe + out)
    stat[-1] = 0
    for i in range(1, len(onboard)):
        new = [0] * (safe + out)
        new[0] = min(stat[0] + b, stat[1] + a)
        for j in range(1, safe + out - 1):
            new[j] = min(stat[j-1], stat[j] + b, stat[j+1] + a)
        new[safe + out - 1] = min(stat[safe + out - 2], stat[safe + out - 1])
        if onboard[i]:
            for j in range(safe, safe + out):
                new[j] = 100000
        stat = new
    return min(stat)