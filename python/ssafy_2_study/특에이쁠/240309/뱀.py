'''
자기 자신과 몸이 충돌 혹은 벽과 충돌 : 게임오버
NxN 정사각 보드 위에서 게임 진행
몇몇 칸에는 사과가 있으며, 사과를 먹으면 사이즈가 커진다.
초기 뱀의 크기는 1이며, 맨 처음엔 오른쪽을 향해 이동한다.
'''
'''
뱀의 이동 매커니즘
1. 먼저 몸을 늘려 머리를 다음칸에 위치시킨다.
    이 때 충돌한다면, 게임 오버
2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과를 먹고 꼬리는 움직이지 않는다.
    사과가 없다면, 몸 길이를 줄여 꼬리가 위치한 칸을 비운다. (몸 길이 동일)

BFS 식을 응용해서 활용 (Q는 뱀의 길이 정보를 담고있으며, 이동 가능한 것 확인은 현 방향만 진행한다.)
방향 변화를 우회전 좌회전으로 주어졌으니, 방향 전환 입력이 주어졌을 때, 어떤 방향으로 바뀔 지 먼저 table작성해 시간 단축
사과를 먹은 경우 Q append + 방문기록만 진행, 사과가 아닌 빈칸인 경우 Q append + 방문기록 + Q popleft + 방문취소
Q == deque()가 종료조건이 아닌, 벽 충돌 및 몸 충돌을 종료 조건으로 설정.
'''
'''
맨 위 맨 좌측을 1행 1열이라고 한 것을 보니, 인덱스를 주의해야한다.
'''
from collections import deque
# 효율적인 계산을 위한 Look-up table
n_dir = [(0,1),(0,-1),(-1,0),(1,0)] # 현재 방향(우좌상하)
c_dir = [((-1,0),(1,0)),((1,0),(-1,0)),((0,-1),(0,1)),((0,1),(0,-1))] # 바꾸는 방향 (좌회전, 우회전)

def bfs():
    now_i = 1
    now_j = 1
    now_dir = (0,1)
    Q = deque()
    matrix[1][1] = 1
    Q.append((1,1))
    cnt = 0
    idx = 0
    while True:
        if cnt == change_lst[idx][0]:
            now_dir = change_dir(now_dir, change_lst[idx][1])
            idx += 1
            if idx == L:
                idx = L-1
        move_i = now_i + now_dir[0]
        move_j = now_j + now_dir[1]
        cnt += 1
        if 1<=move_i<=N and 1<=move_j<=N: # 인덱스를 만족
            if matrix[move_i][move_j] == 1: # 자신의 몸
                return cnt
            elif matrix[move_i][move_j] == 2: # 사과
                Q.append((move_i,move_j))
                now_i = move_i
                now_j = move_j
                matrix[now_i][now_j] = 1
            elif matrix[move_i][move_j] == 0: # 빈 칸
                Q.append((move_i, move_j))
                tail = Q.popleft()
                matrix[tail[0]][tail[1]] = 0
                now_i = move_i
                now_j = move_j
                matrix[now_i][now_j] = 1
        else: # 인덱스를 만족하지 않음.
            return cnt
        
def change_dir(now_dir, input_dir): # 현재 방향에서 입력된 값에 따라 전환하는 방향 값을 도출하는 함수.
    if input_dir == 'D': # 우회전
        check = 1
    elif input_dir == 'L': # 좌회전
        check = 0
    for i in range(4):
        if now_dir == n_dir[i]: # 상단 Look-up table 활용
            return c_dir[i][check]

N = int(input()) # 보드 사이즈
K = int(input()) # 사과 개수
matrix = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
    a,b = map(int,input().split())
    matrix[a][b] = 2 # 사과의 정보 입력

L = int(input()) # 뱀의 방향 전환 입력 정보 (시간초, 방향)
change_lst = []
for _ in range(L):
    sec, dir = input().split()
    sec = int(sec)
    change_lst.append((sec,dir))

print(bfs())