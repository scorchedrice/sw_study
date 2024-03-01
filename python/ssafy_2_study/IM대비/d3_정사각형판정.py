from collections import deque

def check_start(matrix): # 시작 지점을 찾는 함수
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '#':
                return i,j

def check_len_i(matrix, start_i, start_j): # 행을 확인하는 함수
    cnt = 0
    for j in range(start_j, N):
        if matrix[start_i][j] == '#':
            cnt += 1
        elif matrix[start_i][j] == '.':
            break
    return cnt

def check_len_j(matrix, start_i, start_j): # 열을 확인하는 함수
    cnt = 0
    for i in range(start_i, N):
        if matrix[i][start_j] == '#':
            cnt += 1
        elif matrix[i][start_j] == '.':
            break
    return cnt

di = [1,0,1] # 아래 오른쪽 대각(오른쪽아래를향하는)
dj = [0,1,1]
def bfs(start_i, start_j):
    now_i = start_i
    now_j = start_j
    Q_i = deque()
    Q_j = deque()
    matrix[now_i][now_j] = 1
    cnt = 1
    while True:
        for dir in range(3):
            move_i = now_i + di[dir]
            move_j = now_j + dj[dir]
            if 0<=move_i<=N-1 and 0<=move_j<=N-1: # 인덱스 조건을 만족하면서
                if matrix[move_i][move_j] == '#': # 이동 가능하다면
                    matrix[move_i][move_j] = matrix[now_i][now_j] + 1
                    Q_i.append(move_i)
                    Q_j.append(move_j)
                    # 숫자 하나 더하고 큐에 저장
                    cnt += 1
                    # 숫자를 적는 작업을 진행한다면, cnt += 1
        if Q_i == deque():
            break
        now_i = Q_i.popleft()
        now_j = Q_j.popleft()
    return cnt

def two_sector_check(matrix): # bfs를 실행한 이후에
    for i in range(N): # '#'가 또 남아있는지 확인하기 위함
        for j in range(N):
            if matrix[i][j] == '#':
                return True
    return False

def my_determine(matrix, rec_len, my_cnt):
    if two_sector_check(matrix) == True: # 또 다른 막혀있는 칸이 존재하므로
        return 'no'
    result = []
    if matrix[start_i + rec_len -1][start_j + rec_len -1] == rec_len:
        result.append(True) # 대각선 위치에 적은 숫자가 len이라면
    if rec_len**2 == my_cnt: # bfs로 숫자를 센 것이 제곱수와 동일하다면
        result.append(True) # 즉, 해당 영역의 개수가 len**2라면
    if result == [True, True]: # 조건 둘다 만족하면
        return 'yes'
    else:
        return 'no'
    
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix += [list(input())]
    start_i, start_j = check_start(matrix)
    first_i_len = check_len_i(matrix, start_i, start_j) # 먼저 찾은 '#' 기준 가로 (+방향)
    first_j_len = check_len_j(matrix, start_i, start_j) # 세로 (+방향)
    second_i_len = check_len_i(matrix, start_i + first_j_len -1, start_j) # 해당 영역 '#' 맨 왼쪽 맨 아래부터 가로 (+방향)
    second_j_len = check_len_j(matrix, start_i, start_j + first_i_len -1) # 해당 영역 '#' 맨 위 맨 오른쪽부터 세로 (+방향)
    if first_i_len == first_j_len == second_i_len == second_j_len: # 정사각형 내부를 제외하고 프레임이 정사각형과 동일한 경우
        ready = True # 추가 연산을 할 이유가 존재한다.
    else:
        ready = False # 해당 조건을 만족 못하니 bfs와 같은 추가연산을 진행하지 않는다.

    if ready == True: # 추가 연산을 할 자격이 있는 경우
        rec_len = first_i_len # 프레임이 길이가 같은 정사각형 꼴이니 무엇을 할당해도 동일하다.
        my_cnt = bfs(start_i, start_j) # bfs를 하고
        print(f"#{tc} {my_determine(matrix, rec_len, my_cnt)}") # 위에서 정의한 결정함수를 실행
    elif ready == False: # 추가 연산 자격이 없는 경우 (자격미달)
        print(f"#{tc} no")