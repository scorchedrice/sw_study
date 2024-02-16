# BFS(deque)
def find_point(maze, target):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == target:
                return [i,j]

from collections import deque

def BFS(start_i, start_j, end_i, end_j):
    current_i = start_i
    current_j = start_j
    Q_i = deque([])
    Q_j = deque([])
    di = [-1,1,0,0] # 상하좌우
    dj = [0,0,-1,1]
    while True:
        maze[current_i][current_j] = 9
        # 현 위치에 방문 기록
        for dir in range(4):
            DI = current_i + di[dir]
            DJ = current_j + dj[dir]
            if 0<=DI<=15 and 0<=DJ<=15 and (maze[DI][DJ]==0 or maze[DI][DJ]==3):
                if DI == end_i and DJ == end_j:
                    return 1
                else:
                    deque.append(Q_i, DI)
                    deque.append(Q_j, DJ)
                    maze[DI][DJ] = 9
        else:
            if Q_i == deque([]) and Q_j == deque([]):
                return 0
            else:
                current_i = deque.popleft(Q_i)
                current_j = deque.popleft(Q_j)

for testcase in range(1,11):
    tc = int(input())

    maze = []
    for k in range(16):
        maze += [list(map(int,input()))]

    start_i, start_j = find_point(maze, 2)
    end_i, end_j = find_point(maze, 3)
    print(f"#{tc} {BFS(start_i, start_j, end_i, end_j)}")