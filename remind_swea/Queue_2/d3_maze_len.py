from collections import deque

def find_start(maze):
    for k in range(N):
        for l in range(N):
            if maze[k][l] == 2:
                return k, l

def find_end(maze):
    for k in range(N):
        for l in range(N):
            if maze[k][l] == 3:
                return k, l

def BFS(start_i, start_j):
    di = [-1,1,0,0] # 상하좌우
    dj = [0,0,-1,1]
    qi = deque()
    qj = deque()
    now_i = start_i
    now_j = start_j
    maze[start_i][start_j] = 1
    maze[end_i][end_j] = 0
    while True:
        for dir in range(4):
            move_i = now_i + di[dir]
            move_j = now_j + dj[dir]
            if 0<=move_i<=N-1 and 0<=move_j<=N-1:
                if maze[move_i][move_j] == 0:
                    qi.append(move_i)
                    qj.append(move_j)
                    maze[move_i][move_j] = maze[now_i][now_j] + 1
        if qi == deque() and qj == deque():
            return 0
        now_i = qi.popleft()
        now_j = qj.popleft()
        if now_i == end_i and now_j == end_j:
            return maze[now_i][now_j] - 2
        
        
                    
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = []
    for k in range(N):
        maze += [list(map(int,input()))]

    start_i, start_j = find_start(maze)
    end_i, end_j = find_end(maze)
    print(f"#{tc} {BFS(start_i,start_j)}")