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
def DFS(start_i, start_j):
    now_i = start_i
    now_j = start_j
    stack_i = []
    stack_j = []
    while True:
        for dir in range(4):
            move_i = now_i+di[dir]
            move_j = now_j+dj[dir]
            if 0<=move_i<=N-1 and 0<=move_j<=N-1 and maze[move_i][move_j] == '3':
                return 1
            if 0<=move_i<=N-1 and 0<=move_j<=N-1 and maze[move_i][move_j] != '1':
                stack_i += [now_i]
                stack_j += [now_j]
                now_i = move_i
                now_j = move_j
                maze[now_i][now_j] = '1'
                break
        else:
            if stack_i == []:
                return 0
            else:
                now_i = stack_i.pop()
                now_j = stack_j.pop()

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
    print(f"#{tc} {DFS(start_i, start_j)}")