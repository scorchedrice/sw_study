di = [0,1,0,-1] # 오른쪽, 아래, 왼쪽, 위로 .. 이 사이클이 반복되도록 해야함.
dj = [1,0,-1,0]
def dfs():
    cnt = 0
    dir = 0
    now_i = 0
    now_j = 0 # 시작지점
    while True:
        cnt += 1
        matrix[now_i][now_j] = cnt
        if cnt == N**2:
            return
        move_i= now_i + di[dir]
        move_j= now_j + dj[dir]
        if 0<=move_i<=N-1 and 0<=move_j<=N-1 and matrix[move_i][move_j] == 0:
            now_i = move_i
            now_j = move_j
        else:
            dir += 1
            if dir == 4:
                dir = 0
            now_i = now_i + di[dir]
            now_j = now_j + dj[dir]
        
        
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    dfs()
    print(f"#{tc}")
    for _ in range(N):
        print(*matrix[_])