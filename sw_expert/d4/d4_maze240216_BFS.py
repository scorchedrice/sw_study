# BFS

def find_point(maze, target):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == target:
                return [i,j]
            
def BFS(start_i, start_j, end_i, end_j):
    current_i = start_i
    current_j = start_j
    Q_i = []
    Q_j = []
    di = [-1,1,0,0] # 상하좌우
    dj = [0,0,-1,1]
    while True:
        maze[current_i][current_j] = 9
        for dir in range(4): # 현 위치에서 4방향, 진행가능 여부를 판별해 Q에 push
            move_i = current_i + di[dir]
            move_j = current_j + dj[dir]
            if 0<=move_i<=15 and 0<=move_j<=15 and (maze[move_i][move_j] == 0 or maze[move_i][move_j] == 3):
                if move_i == end_i and move_j == end_j:
                    # 조건을 따졌을 때, push할 것이 도착지점 index라면 더 계산할 필요 없음
                    return 1
                else:
                    Q_i += [move_i]
                    Q_j += [move_j]
                    maze[move_i][move_j] = 9
                    # 갈 수 있는 후보들 큐에 넣고 방문 기록 남기기
        else:
            if Q_i == [] and Q_j == []:
                return 0
            else:
                current_i = Q_i.pop(0)
                current_j = Q_j.pop(0)



for testcase in range(1,11):
    tc = int(input())

    maze = []
    for k in range(16):
        maze += [list(map(int,input()))]

    start_i, start_j = find_point(maze, 2)
    end_i, end_j = find_point(maze, 3)
    print(f"#{tc} {BFS(start_i, start_j, end_i, end_j)}")