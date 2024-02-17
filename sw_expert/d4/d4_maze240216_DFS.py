# 미로는 16*16 사이즈
'''
DFS, BFS 모두 활용 가능
'''
# 시작점과 종료지점을 찾기 위한 함수 정의
def find_point(maze, target):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == target:
                return [i,j]

def DFS(start_i, start_j, end_i, end_j):
    current_i = start_i
    current_j = start_j
    stack_i= []
    stack_j= []
    di = [-1,1,0,0] # 상하좌우
    dj = [0,0,-1,1]
    while True:
        maze[current_i][current_j] = 9 # 방문했다는 기록을 남긴다.
        for dir in range(4):
            move_i = di[dir] + current_i
            move_j = dj[dir] + current_j
            if 0<=move_i<=15 and 0<=move_j<=15 and (maze[move_i][move_j] == 0 or maze[move_i][move_j] == 3):
                # 인덱스 조건을 만족하면서 이동이 가능한 경우라면
               stack_i += [current_i]
               stack_j += [current_j] # 현 위치를 stack에 push하고
               current_i = move_i
               current_j = move_j # 해당 위치로 이동한다.
               if current_i == end_i and current_j == end_j:
                   return 1 # 이동한 곳이 출구라면 1 도출
               break # for문 종료
        else:
            if stack_i == [] and stack_j == []:
                # stack이 비어있는 경우
                return 0
            else:
                current_i = stack_i.pop()
                current_j = stack_j.pop()
                # 아니라면 (갈 곳이 없다면) 이전 위치로 돌아간다.
    
for testcase in range(1,11):
    tc = int(input())

    maze = []
    for k in range(16):
        maze += [list(map(int,input()))]

    start_i, start_j = find_point(maze, 2)
    end_i, end_j = find_point(maze, 3)
    print(f"#{tc} {DFS(start_i, start_j, end_i, end_j)}")
