# 오셀로

def can_i_change(i,j,stone,N):
    game_map[i][j] = stone # 돌을 놓기

    if stone == 1: # 흑돌인경우
        another_stone = 2
    elif stone == 2: # 백돌인경우
        another_stone = 1

    for dir in range(8): # 8가지 방향에 대한 탐색 진행
        coord_stack_i= [] # 내가 확인한 방향을 기록하기 위해
        coord_stack_j = []
        current_i = i + di[dir] # 해당하는 방향으로 한칸 이동하고
        current_j = j + dj[dir]
        while 0 <= current_i <= N-1 and 0<= current_j <= N-1 and game_map[current_i][current_j] == another_stone:
            # 좌표조건을 만족하고 다른 돌이 있는 것을 확인한다면 혹은 비어있다면
            coord_stack_i += [current_i] # stack에 추가하고
            coord_stack_j += [current_j]
            current_i += di[dir] # 한칸 더 이동한다.
            current_j += dj[dir]
                
        if  0 <= current_i <= N-1 and 0 <= current_j <= N-1 and game_map[current_i][current_j] == stone:
            # while문에 걸리지 않고 index 조건을 만족함과 동시에 그 좌표에 내가 놓았던 돌이 있다면
            for my_stack in range(len(coord_stack_i)):
                game_map[coord_stack_i[my_stack]][coord_stack_j[my_stack]] = stone # 내가 놓았던 돌로 뒤집는다.
    

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
        can_i_change(i_input-1,j_input-1,stone,N) # 내가 돌을 뒤집을 수 있는지 계산.
    
    count_black = 0
    count_white = 0
    for m in range(N):
        for n in range(N):
            if game_map[m][n] == 1:
                count_black += 1
            elif game_map[m][n] == 2: # 놓는 횟수가 정해져 있으니 else로 처리하면 공백인 경우도 셀 수 있음!!!!
                count_white += 1
    print(f"#{tc} {count_black} {count_white}")
