from collections import deque

def find_start(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i,j
def find_end(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '3':
                return i, j

def BFS(start_i, start_j):
    Q_i = deque()
    Q_j = deque()
    now_i = start_i
    now_j = start_j
    
    while True:
        maze[now_i][now_j] = '1'
        for dir in range(4):
            move_i = now_i + di[dir]
            move_j = now_j + dj[dir]
            if 0<=move_i<=N-1 and 0<=move_j<=N-1 and maze[move_i][move_j] != '1':
                deque.append(Q_i, move_i)
                deque.append(Q_j, move_j)
        
        if Q_i == deque():
            return 0
        
        now_i = deque.popleft(Q_i)
        now_j = deque.popleft(Q_j)
        if now_i == end_i and now_j == end_j:
            return 1
        
di = [-1,1,0,0] # 상 하 좌 우
dj = [0,0,-1,1]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        maze += [list(input())]
    start_i, start_j = find_start(maze)
    end_i, end_j = find_end(maze)
    print(f"#{tc} {BFS(start_i, start_j)}")