# 탈주범 검거
'''
문제 풀이 방향
1. 터널 별 통과 가능한 터널들을 정리한다. (함수로 정의하던가 look-up table)
2. 시간당 1의 거리를 움직일 수 있으므로, dij사용 x, bfs
index는 정상적으로 주어짐
'''
'''
주어지는 input값 정보
첫 줄 tc
둘째줄 N, M (size), R, C(시작 위치), L(시간)
'''
# 터널 정보 정리
'''
mi,mj : 이동 가능 후보 (ci + di[dir], cj + dj[dir])
ci,cj : 현 위치
1. (상하좌우 연결) : mi,mj에 터널이 존재하고 그 터널이 ci,cj와 연결되어 있다면 이동 가능
2. (상하 연결) : mi,mj가 상/하이면서 해당 위치의 터널이 ci,cj와 연결되어 있다면 이동 가능
3. (좌우 연결) : mi,mj가 좌/우이면서 해당 위치의 터널이 ci,cj와 연결되어 있다면 이동 가능
4. (상우 연결) : mi,mj가 상/우이면서 ...
5. (하우 연결) : mi,mj가 하/우이면서 ...
6. 하좌
7. 상좌
'''
from pprint import pprint
from collections import deque
# BFS

# 해당 파이프가 어디를 향하는지 (0 : 상, 1 : 우, 2: 하, 3 : 좌), index가 해당 파이프 의미
dir_pipe = [[],[0,1,2,3],[0,2],[1,3],[0,1],[1,2],[2,3],[0,3]]

def dir_convert(current_dir):
    result = current_dir + 2
    if result > 3:
        result = result - 4
    return result

def cal_move(ci,cj,mi,mj,current_dir):
    # ci,cj의 터널 정보를 받고, mi,mj의 터널 위치와 비교하며 이동 가능 여부를 판단하는 함수
    if matrix[mi][mj] == 0:
        return False # 해당 경로가 0으로 터널이 존재하지 않으면 False
    start_pipe_info = dir_pipe[matrix[ci][cj]]
    end_pipe_info = dir_pipe[matrix[mi][mj]]
    nxt_pipe_dir = dir_convert(current_dir) # 이동할 방향에 존재하는 pipe 의 반대 방향 (current_dir와 마주보는 방향)
    if current_dir in start_pipe_info and nxt_pipe_dir in end_pipe_info:
        return True
    else:
        return False

di = [-1,0,1,0] # 상우하좌
dj = [0,1,0,-1]

def bfs(start_i, start_j, end_time):
    global pivot
    Qi = deque()
    Qj = deque()
    Qi.append(start_i)
    Qj.append(start_j)
    visited = [[0]*M for _ in range(N)]
    visited[start_i][start_j] = 1
    while Qi:
        ci = Qi.popleft()
        cj = Qj.popleft()
        for dir in range(4):
            mi = ci + di[dir]
            mj = cj + dj[dir] # 이동 가능 후보
            if 0<=mi<N and 0<=mj<M and visited[mi][mj] == 0: # index를 만족하고 방문한 적이 없다면
                if cal_move(ci,cj,mi,mj,dir) == False: # 해당 위치가 이동 불가능 하면 넘어가고
                    continue
                # 상단의 if에 걸리지 않음 == 이동 가능함
                visited[mi][mj] = visited[ci][cj] + 1 # 방문기록
                pivot = visited[mi][mj]
                Qi.append(mi)
                Qj.append(mj)
        else:
            # for 문이 다 끝나고
            if pivot == end_time:
                break
    return visited

# T = int(input())
# for tc in range(1,T+1):
N, M, si, sj, T = map(int,input().split())
# N x M and start i start j and Time
matrix = []
for k in range(N):
    matrix.append(list(map(int,input().split())))
pivot = 0
pprint(bfs(si,sj,T))