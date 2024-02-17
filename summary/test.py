# 오셀로
# 1 : 흑, 2 : 백 , 흑 선공

def can_i_change(i,j,stone):
    
    if stone == 1: # 흑돌인경우
        another_stone = 2
    elif stone == 2: # 백돌인경우
        another_stone = 1

    for dir in range(8): # 8가지 방향에 대한 탐색 진행
        current_i = i
        current_j = j
        coord_stack_i= [] # 내가 확인한 방향을 기록하기 위해
        coord_stack_j = []
        while 0 <= current_i + di[dir] <= N-1 and 0<= current_j + dj[dir] <= N-1:
            current_i = current_i + di[dir] # 해당하는 방향으로 한칸 이동하고
            current_j = current_j + dj[dir]
            
            if game_map[current_i][current_j] == another_stone: # 그 좌표가 내가 놓았던 돌의 색상이 아니라면
                coord_stack_i += [current_i]
                coord_stack_j += [current_j]
    
            elif game_map[current_i][current_j] == stone and coord_stack_i == []: # 내가 놓았던 돌 색상과 동일하고 my_stack이 비어있다면
                break
                
            elif game_map[current_i][current_j] == stone: # 그 좌표가 내가 놓았던 돌의 색상과 동일하다면
                for my_stack in range(len(coord_stack_i)):
                    game_map[coord_stack_i[my_stack]][coord_stack_j[my_stack]] = stone # 내가 놓았던 돌로 뒤집는다.
                break
            
            else:
                break
    return

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) # N : size, M : 돌을 놓는 횟수
    game_map = [[0]*N for _ in range(N)]

    game_map[N//2][N//2] = 2
    game_map[N//2 - 1][N//2 - 1] = 2
    game_map[N//2 - 1][N//2] = 1
    game_map[N//2][N//2 - 1] = 1 # game_map 설정

    di = [-1,1,0,0,-1,-1,1,1] #북 남 서 동 우상 좌상 우하 좌하
    dj = [0,0,-1,1,1,-1,1,-1]

    for _ in range(M):
        j_input, i_input, stone = map(int, input().split())
        i = i_input-1
        j = j_input-1
        game_map[i][j] = stone # 돌을 놓고
        can_i_change(i,j,stone) # 내가 돌을 뒤집을 수 있는지 계산.
    
    count_black = 0
    count_white = 0
    for m in range(N):
        for n in range(N):
            if game_map[m][n] == 1:
                count_black += 1
            elif game_map[m][n] == 2:
                count_white += 1
    print(f"#{tc} {count_black} {count_white}")
