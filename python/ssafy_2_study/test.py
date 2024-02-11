# 8-4 미로탈출
# N*M maze (4이상 200이하)
# start = 1,1 ... index 조심!!!
# exit = N,M
# monster : 0, safe : 1
'''
아이스크림 문제와 동일하게 기록하며 이동한다.
return값을 stack으로 한다면, 이동한 기록을 확인할 수 있다.
 ----- 불필요한 이동이 생길 수 있음.
이 stack의 길이를 답으로 할 수 있다.
'''

''' test1
5 6
101010
111111
000001
111111
111111
ans : 10
'''
''' test2
6 6
111111
111111
001001
110011
001111
111111 
ans : 11
'''
''' test3
6 6
111111
000001
111111
010000
111000
001111
ans : 19
'''
def maze_runner(maze_map):
    current_i = 0
    current_j = 0
    di = [-1, 1, 0, 0] # 북 남 동 서
    dj = [0, 0, 1, -1]
    maze_stack_i = []
    maze_stack_j = []
    while True:
        for dir in range(4): # 4방향 탐색
            if 0 <= current_i + di[dir] < N and 0 <= current_j + dj[dir] < M and maze_map[current_i+di[dir]][current_j+dj[dir]] == 1:
                # index범위 조건을 만족하면서 해당 위치에 1이 있다면(이동가능하다면)
                maze_stack_i += [current_i + di[dir]]
                maze_stack_j += [current_j + dj[dir]] # 이동 가능한 후보를 스택에 추가한다.
        for _ in range(len(maze_stack_i)):
            if maze_map[maze_stack_i[_]][maze_stack_j[_]] == 1: # 해당 위치가 방문한 적이 없다면
                maze_map[maze_stack_i[_]][maze_stack_j[_]] = maze_map[current_i][current_j] + 1 # 주변 위치에 넘버링을 한다.
        
        if maze_stack_i == []:
            return '도망갈 수 없습니다.'

        current_i = maze_stack_i[0] # 라이브러리 없이 popleft()를 구현
        current_j = maze_stack_j[0]
        del maze_stack_i[0]
        del maze_stack_j[0]
        if current_i == N-1 and current_j == M-1:
            return maze_map[N-1][M-1]
    return

N, M = map(int, input().split())
maze_map = [list(map(int, input())) for _ in range(N)]
print(maze_runner(maze_map))
print('------')
for _ in range(N):
    print(maze_map[_])