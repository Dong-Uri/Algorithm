def solution(board, skill):
    # left = []
    # for s in skill:
    #     if s[0] == 1:
    #         for i in range(s[1], s[3] + 1):
    #             for j in range(s[2], s[4] + 1):
    #                 board[i][j] -= s[5]
    #     else:
    #         left.append(s)
    # answer = 0
    # lst = []
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if board[i][j] > 0:
    #             answer += 1
    #         else:
    #             lst.append([i, j])
    # for i, j in lst:
    #     for s in left:
    #         if s[1] <= i <= s[3] and s[2] <= j <= s[4]:
    #             board[i][j] += s[5]
    #             if board[i][j] > 0:
    #                 answer += 1
    #                 break
    
#     dest = []
#     heal = []
#     for s in skill:
#         if s[0] == 1:
#             dest.append(s)
#         else:
#             heal.append(s)
    
#     answer = 0
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             a = board[i][j]
#             for s in dest:
#                 if s[1] <= i <= s[3] and s[2] <= j <= s[4]:
#                     a -= s[5]
#             for s in heal:
#                 if a > 0:
#                     break
#                 if s[1] <= i <= s[3] and s[2] <= j <= s[4]:
#                     a += s[5]
#             if a > 0:
#                 answer += 1

    # import numpy as np
#     np_board = np.array(board)
    
#     skill_map = []
#     for s in skill:
#         map = [[0] * len(board[0]) for _ in range(len(board))]
#         for i in range(s[1], s[3]+1):
#             for j in range(s[2], s[4]+1):
#                 map[i][j] = (2 * s[0] - 3) * s[5]
#         np_board += np.array(map)
        
#     answer = 0
#     for line in np_board:
#         for x in line:
#             if x > 0:
#                 answer += 1
    change = [[0] * len(board[0]) for _ in range(len(board))]
    for s in skill:
        change[s[1]][s[2]] += (2 * s[0] - 3) * s[5]
        if s[3] < len(board) - 1:
            change[s[3] + 1][s[2]] += (3 - 2 * s[0]) * s[5]
        if s[4] < len(board[0]) - 1:
            change[s[1]][s[4] + 1] += (3 - 2 * s[0]) * s[5]
        if s[3] < len(board) - 1 and s[4] < len(board[0]) - 1:
            change[s[3] + 1][s[4] + 1] += (2 * s[0] - 3) * s[5]
    for i in range(len(board)):
        a = change[i][0]
        for j in range(1, len(board[0])):
            a += change[i][j]
            change[i][j] = a
    for j in range(len(board[0])):
        a = change[0][j]
        for i in range(1, len(board)):
            a += change[i][j]
            change[i][j] = a
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + change[i][j] > 0:
                answer += 1
    return answer