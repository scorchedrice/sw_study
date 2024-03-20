from collections import deque

di = [1,-1,0,0]
dj = [0,0,-1,1]

def bfs(si,sj):
    global data
    room = matrix[si][sj]
    ci = si
    cj = sj
    Qi = deque()
    Qj = deque()
    Qi.append(ci)
    Qj.append(cj)
    tmp = 0
    v = [[0 for _ in range(N)] for _ in range(N)]
    v[ci][cj] = 1
    while True:
        for dir in range(4):
            mi = ci + di[dir]
            mj = cj + dj[dir]
            if 0<=mi<N and 0<=mj<N and v[mi][mj] == 0:
                if matrix[mi][mj] - matrix[ci][cj] == 1:
                    v[mi][mj] = v[ci][cj] + 1
                    tmp = v[ci][cj] + 1
                    Qi.append(mi)
                    Qj.append(mj)
        if Qi == deque():
            break
        ci = Qi.popleft()
        cj = Qj.popleft()
    if data[] # 여기에 데이터 값을 비교해서 데이터를 계속 전환하는 과정을 추가
    

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int,input().split())))
    data = (-9, 0)
    for i in range(N):
        for j in range(N):
            bfs(i,j)
    
    result = data[-1]
    room_num = abs(result[1])
    cnt =  result[0]
    print(f"#{tc} {room_num} {cnt}")