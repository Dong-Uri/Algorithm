def solution(board, aloc, bloc):
    
    def player_move_A(aloc, bloc, cnt):
        result_lst = []
        if not board[aloc[0]][aloc[1]]:
            return cnt
        check = True
        if aloc[0] > 0 and board[aloc[0]-1][aloc[1]]:
            check = False
            board[aloc[0]][aloc[1]] = 0
            aloc[0] -= 1
            result_lst.append(player_move_A(bloc, aloc, cnt+1))
            aloc[0] += 1
            board[aloc[0]][aloc[1]] = 1
        if aloc[0] < len(board)-1 and board[aloc[0]+1][aloc[1]]:
            check = False
            board[aloc[0]][aloc[1]] = 0
            aloc[0] += 1
            result_lst.append(player_move_A(bloc, aloc, cnt+1))
            aloc[0] -= 1
            board[aloc[0]][aloc[1]] = 1
        if aloc[1] > 0 and board[aloc[0]][aloc[1]-1]:
            check = False
            board[aloc[0]][aloc[1]] = 0
            aloc[1] -= 1
            result_lst.append(player_move_A(bloc, aloc, cnt+1))
            aloc[1] += 1
            board[aloc[0]][aloc[1]] = 1
        if aloc[1] < len(board[0])-1 and board[aloc[0]][aloc[1]+1]:
            check = False
            board[aloc[0]][aloc[1]] = 0
            aloc[1] += 1
            result_lst.append(player_move_A(bloc, aloc, cnt+1))
            aloc[1] -= 1
            board[aloc[0]][aloc[1]] = 1
        if check:
            return cnt
        if result_lst:
            if cnt % 2:
                return max(result_lst)
            else:
                min_r = 25
                for r in result_lst:
                    if r % 2 and r < min_r:
                        min_r = r
                return min_r
        else:
            return False
        
    def player_move_B(aloc, bloc, cnt):
        result_lst = []
        if not board[aloc[0]][aloc[1]]:
            return cnt
        check = True
        if aloc[0] > 0 and board[aloc[0]-1][aloc[1]]:
            check = False
            board[aloc[0]][aloc[1]] = 0
            aloc[0] -= 1
            result_lst.append(player_move_B(bloc, aloc, cnt+1))
            aloc[0] += 1
            board[aloc[0]][aloc[1]] = 1
        if aloc[0] < len(board)-1 and board[aloc[0]+1][aloc[1]]:
            check = False
            board[aloc[0]][aloc[1]] = 0
            aloc[0] += 1
            result_lst.append(player_move_B(bloc, aloc, cnt+1))
            aloc[0] -= 1
            board[aloc[0]][aloc[1]] = 1
        if aloc[1] > 0 and board[aloc[0]][aloc[1]-1]:
            check = False
            board[aloc[0]][aloc[1]] = 0
            aloc[1] -= 1
            result_lst.append(player_move_B(bloc, aloc, cnt+1))
            aloc[1] += 1
            board[aloc[0]][aloc[1]] = 1
        if aloc[1] < len(board[0])-1 and board[aloc[0]][aloc[1]+1]:
            check = False
            board[aloc[0]][aloc[1]] = 0
            aloc[1] += 1
            result_lst.append(player_move_B(bloc, aloc, cnt+1))
            aloc[1] -= 1
            board[aloc[0]][aloc[1]] = 1
        if check:
            return cnt
        if result_lst:
            if cnt % 2:
                min_r = 25
                for r in result_lst:
                    if not r % 2 and r < min_r:
                        min_r = r
                return min_r
            else:
                return max(result_lst)
        else:
            return False
        
    print(player_move_A(aloc, bloc, 0))
    print(player_move_B(aloc, bloc, 0))
        
    ans = player_move_A(aloc, bloc, 0)
    if ans != 25:
        return ans
    else:
        return player_move_B(aloc, bloc, 0)