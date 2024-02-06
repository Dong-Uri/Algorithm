def solution(m, n, board):
    answer = 0
    
    dap = []
    for i in range(m):
        board[i] = list(board[i])
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                b = board[i][j]
                if b == '0':
                    continue
                if board[i][j + 1] == b and board[i + 1][j] == b and board[i + 1][j + 1] == b:
                    dap.append([i, j])
                    dap.append([i, j + 1])
                    dap.append([i + 1, j])
                    dap.append([i + 1, j + 1])
        
        if not dap:
            break
            
        while dap:
            i, j = dap.pop()
            if board[i][j] != '0':
                board[i][j] = '0'
                answer += 1
                
        for j in range(n):
            bls = []
            for i in range(m):
                if board[i][j] != '0':
                    bls.append(board[i][j])
                    board[i][j] = '0'
            i = m - 1
            while bls:
                b = bls.pop()
                board[i][j] = b
                i -= 1

    return answer