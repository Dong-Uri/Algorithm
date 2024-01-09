def solution(n, t, m, p):
    
    # 한글자씩 진행
    num = 0
    game_ord = '0' # 전체 게임 진행 문자열
    while True:
        num += 1
        
        # old_num에서 new_num으로 진수 변환
        old_num = num
        new_num = ''
        while old_num:
            character = old_num % n
            if character < 10:
                character = str(character)
            else:
                character = chr(character + 55)
            new_num = character + new_num
            old_num = old_num // n
            
        game_ord += new_num
        if len(game_ord) > t * m:
            break
    
    # 전체 게임 진행 중 내가 말해야할 값 지정
    answer = ''
    for i in range(t):
        answer += game_ord[i * m + p - 1]
    return answer