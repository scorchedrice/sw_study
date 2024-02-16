'''
N과 미로 정보를 입력받은 후 시작지점과 도착지점을 찾는다. (start, end)
end와 연결되어 있는 칸 (i index차이 + j index차이가 1인경우)에 도달하면 반복문 종료
'''
'''
BFS를 적용하여 숫자를 늘려가며 값을 교체하며 전진한다.
단, 큐에 방문 가능 위치를 추가할 때, 현 위치의 +1을 기록하면서 나아간다.
이를 통해 거리에 대한 정보를 기록하고 다시 이를 고려하지 않도록 한다.
(시작은 2부터 하기에, 1이 아니면서 0이 아닌 경우는 방문 가능한 위치에 해당하고
    그 외의 경우는 방문한 적이 있어 더이상 고려할 필요가 없는 구역이다.
        더불어 2 부터 하나씩 늘려가며 기록했기에, 거리에 대한 정보도 담고있다.)
'''
# deque library사용하면 popleft 활용가능
def my_popleft(Q):
    result = Q[0]
    del Q[0]
    return result
# 시작점을 찾는 (2가 기록된 좌표를 찾는) 함수
def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
# 종료지점을 찾는 (3이 기록된 좌표를 찾는) 함수
def find_end():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                return i, j
             
# BFS로 기록을 진행하고 출구 인근에 먼저 도달하는 케이스가 발생하면
# 해당 위치에 기록된 값을 활용해 최단거리를 return 하는 함수
def find_exit(start_i, start_j, end_i, end_j):
    # 우선 상 하 좌 우의 변화값을 활용하기 위해 di, dj값을 정의한다.
    # 더불어 시작지점을 현 위치로 하고(미로 탈출 시작)
    # 방문 가능 여부를 기록하기 위한 Q를 정의한다.
    current_i = start_i
    current_j = start_j
    di = [-1,1,0,0] # 상하좌우
    dj = [0,0,-1,1]
    Q_i = []
    Q_j = []
     
    while True:
        for dir in range(4): # 상 하 좌 우 4 방향을 확인한다.
            if 0<=current_i + di[dir]<N and 0<=current_j + dj[dir]<N:
                if maze[current_i + di[dir]][current_j + dj[dir]] == 0:
                    # 이동할 위치가 인덱스 조건을 만족함과 동시에 해당 위치가 통로면
                    Q_i += [current_i + di[dir]]
                    Q_j += [current_j + dj[dir]]
                    # 방문이 가능한 위치를 큐에 추가한다.
                    maze[current_i + di[dir]][current_j + dj[dir]] = maze[current_i][current_j] + 1
                    # 더불어 미리 기록을 해둔다 (현 위치 더하기 1)
         
        # 도착하지 못하는 경우가 발생하는 경우를 위한 조건문
        if Q_i == []:
            return 0
        
        # 직접 가보자
        current_i = my_popleft(Q_i)
        current_j = my_popleft(Q_j)
 
        # 만약 도착지점옆이라면 결과를 도출한다.
        # 2부터 카운트를 시작했기에 2를 빼준 것을 결과로 return
        if (abs(current_i - end_i) == 1 and (current_j == end_j)) or ((current_i == end_i) and abs(current_j - end_j) == 1):
            return maze[current_i][current_j] - 2
         
 
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
 
    start_i, start_j = find_start()
    end_i, end_j = find_end()
     
    print(f"#{tc} {find_exit(start_i, start_j, end_i, end_j)}")