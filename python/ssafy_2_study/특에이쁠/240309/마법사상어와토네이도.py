'''
사전 정의한 look-up table
- 방향에 따라 흩날리는 모래 table
- 방향에 따른 변화 리스트/알파 위치 리스트, 방향 전환을 확인 할 방향 체크 리스트

정의한 함수
- 90도로 table을 돌리는 함수
- 방향에 맞는 table을 통해 흩날리는 모래를 할당 하는 함수
- 위 함수를 활용해 모래 정보를 실시간으로 수정(할당) + 밖으로 나가는 모래를 계산하는 함수
- 방향 전환을 해야 하는지 확인하는 함수
'''
'''
문제풀이 방향
1. table, 방향 관련 정보들을 기록
2. 이동 후 흩날리는 모래 정보를 기록하는 함수를 정의한다.
    밖으로 나가는 모래를 실시간으로 count, table을 적극 활용해 실시간 모래정보 반영
3. 방향 전환 여부를 판단하고 방향 전환 혹은 반복문 종료
'''

from copy import deepcopy
table_left = [[0,0,0.02,0,0],[0,0.1,0.07,0.01,0],[0.05,0,0,0,0],[0,0.1,0.07,0.01,0],[0,0,0.02,0,0]]

def change_90(table): # table을 사전 기록하기 위함
    matrix = []
    for j in range(4,-1,-1):
        memory = []
        for i in range(5):
            memory.append(table[i][j])
        matrix.append(memory)
    return matrix

table_down = change_90(table_left)
table_right = change_90(table_down)
table_up = change_90(table_right)
alpha_lst = [(2,1),(3,2),(2,3),(1,2)] # 좌 하 우 상

def scatter(dir, sand): # 흩날리는 모래 정보 반영, 이후 arr 반영 함수에 활용하기 위함.
    if dir == 0:
        c_table = deepcopy(table_left)
    elif dir == 1:
        c_table = deepcopy(table_down)
    elif dir == 2:
        c_table = deepcopy(table_right)
    else:
        c_table = deepcopy(table_up)
    scattered_sand = 0
    for i in range(5):
        for j in range(5):
            if c_table[i][j] != 0:
                c_table[i][j] = int(c_table[i][j] * sand)
                scattered_sand += c_table[i][j]
    c_table[alpha_lst[dir][0]][alpha_lst[dir][1]] = sand - scattered_sand
    return c_table

def assign_sand(now_i,now_j, dir, sand): # 위 함수를 활용해 arr 실시간 수정, 나가는 모래 양 계산
    global out_sand
    global arr
    c_table = scatter(dir,sand)
    arr[now_i][now_j] = 0
    for i in range(5):
        for j in range(5):
            if c_table[i][j] != 0:
                di = i-2
                dj = j-2
                in_arr_i = now_i + di
                in_arr_j = now_j + dj
                if 0<=in_arr_i<=N-1 and 0<=in_arr_j<=N-1:
                    arr[in_arr_i][in_arr_j] += c_table[i][j]
                else:
                    out_sand += c_table[i][j]

dir_info = [(0,-1),(1,0),(0,1),(-1,0)] # 좌 하 우 상
check_change = [(1,0),(0,1),(-1,0),(0,-1)] # 좌 이동 중 하 확인, 하 이동 중 우 확인 ...

def change_dir(now_i, now_j, c_dir): # 방향 전환 여부 판단 (달팽이 모양 진행 위함)
    c_now_i = now_i + check_change[c_dir][0]
    c_now_j = now_j + check_change[c_dir][1]
    if 0<=c_now_i<=N-1 and 0<=c_now_j<=N-1 and v[c_now_i][c_now_j] == 0:
        c_dir = c_dir + 1
        if c_dir == 4:
            c_dir = 0
    return c_dir

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
v = [[0 for _ in range(N)] for _ in range(N)] # visited활용해 달팽이 형태로 진행
out_sand = 0
dir = 0
now_i = N//2
now_j = now_i # 시작지점
v[now_i][now_j] = 1
while True:
    mv_i = now_i + dir_info[dir][0]
    mv_j = now_j + dir_info[dir][1]
    if 0<=mv_i<=N-1 and 0<=mv_j<=N-1 and v[mv_i][mv_j] == 0:
        v[mv_i][mv_j] = 1
        now_i = mv_i
        now_j = mv_j
    else: # N은 홀수로만 주어지기에 idx를 벗어난다 == 달팽이 꼴 진행 종료
        break
    assign_sand(now_i,now_j,dir,arr[now_i][now_j]) # 모래 정보 실시간 반영
    dir = change_dir(now_i, now_j, dir) # 방향전환 여부 판단
print(out_sand)