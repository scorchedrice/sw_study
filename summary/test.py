# 8방향 설정
di = [0, 1, 1, 1, 0, -1, -1, -1]  
dj = [1, 1, 0, -1, -1, -1, 0, 1]
 
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    doll = [list(map(int, input().split())) for _ in range(M)]  # 좌표 및 돌색 입력
    arr = [[0]*N for _ in range(N)] # 보드판 배열 입력
 
    B = 1   # 흑돌
    W = 2   # 백돌
 
    # 게임 시작 돌 위치      
    arr[N//2-1][N//2-1] = W   
    arr[N//2-1][N//2] = B
    arr[N//2][N//2-1] = B
    arr[N//2][N//2] = W
 
    # 입력된 좌표 및 돌색 배열에 추가하기
    for i, j, color in doll:
        arr[i-1][j-1] = color
        # 8방향을 탐색하기
        for k in range(8):
            ni = i-1 + di[k]
            nj = j-1 + dj[k]
            change = []         # 돌의 색을 바꿀 좌표를 넣을 리스트 생성
  
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != color:   # 범위내에 있고, 색이 다를 때,
                change.append((ni,nj))  # 리스트에 좌표를 넣어준다.
                ni = ni + di[k]         # 좌표를 이동 한다.
                nj = nj + dj[k]
  
                if 0 <= ni <N and 0 <= nj < N and arr[ni][nj] == color:   # 범위 내에 있고, 색이 같을 때,
                    for p, q in change:        # 넣어뒀던 색을 바꿀 좌표를 하나씩 꺼낸다
                        arr[p][q] = color       # 색을 바꿔준다.
 
    cnt_b = 0       # 검은 돌의 개수를 넣을 변수
    cnt_w = 0       # 하얀 돌의 개수를 넣을 변수
  
    for i in range(N):             # 보드판을 다 돌면서,
        for j in range(N):
            if arr[i][j] == B:   # 검은색 돌을 발견하면,
                cnt_b += 1          # 검은 돌의 개수를 추가한다.
  
            elif arr[i][j] == W: # 하얀 돌을 발견하면,
                cnt_w += 1          # 하얀 돌의 개수를 추가한다.
  
    print(f'#{test_case} {cnt_b} {cnt_w}')