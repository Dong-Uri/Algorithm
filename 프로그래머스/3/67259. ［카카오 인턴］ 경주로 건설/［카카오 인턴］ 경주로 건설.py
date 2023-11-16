import heapq
import copy

def solution(board):
    answer = 0
    ways = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    now = [[0, 0, 0, 0], [0, 1, 0, 0]] # 현재비용, 진행방향, x좌표, y좌표
    board[0][0] = 1
    bboard = [copy.deepcopy(board) for _ in range(4)]
    while now:
        n = heapq.heappop(now)
        if answer != 0 and n[0] <= answer:
            break
        if answer != 0 and n[0] >= answer:
            break
        for i, w in enumerate(ways):
            new = [n[2] + w[0], n[3] + w[1]]
            if new[0] < 0 or new[0] >= len(board[0]):
                continue
            if new[1] < 0 or new[1] >= len(board):
                continue
            if board[new[0]][new[1]] == 1:
                continue
            if (n[1] + i) % 2:
                if bboard[i][n[2]][n[3]] == 0 or bboard[i][n[2]][n[3]] > n[0] + 500:
                    bboard[i][n[2]][n[3]] = n[0] + 500
                    heapq.heappush(now, [n[0] + 500, i, n[2], n[3]])
            elif n[1] == i:
                if bboard[i][new[0]][new[1]] == 0 or bboard[i][new[0]][new[1]] > n[0] + 100:
                    bboard[i][new[0]][new[1]] = n[0] + 100
                    heapq.heappush(now, [n[0] + 100, i, new[0], new[1]])
                    if new[0] == len(board[0]) - 1 and new[1] == len(board) - 1:
                        if answer < n[0] + 100:
                            answer = n[0] + 100
            else:
                continue
            
    return answer