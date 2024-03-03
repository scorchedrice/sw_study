# 정지 상 우 하 좌
dx = [0,0,1,0,-1]
dy = [0,-1,0,1,0]

T = int(input())
for tc in range(1,T+1):
    M, A = map(int,input().split())
    # M은 이동 횟수, A는 설치 충전기 개수
    move_A = list(map(int,input().split()))
    move_B = list(map(int,input().split()))
    matrix = []
    for _ in range(A):
        matrix.append(tuple(map(int,input().split())))
        # 좌표 x, 좌표 y, 충전 범위, 충전 파워
    cnt = 0
    Ax, Ay = [1,1]
    Bx, By = [10,10]
    result = 0
    idx = 0
    while True:
        
        use_A = []
        use_B = []
        for i in range(A):
            Tx = matrix[i][0]
            Ty = matrix[i][1]
            dist_A = abs(Ax - Tx) + abs(Ay - Ty)
            dist_B = abs(Bx - Tx) + abs(By - Ty)
            if dist_A <= matrix[i][2]:
                use_A.append(matrix[i][3])
            else:
                use_A.append(0)
            if dist_B <= matrix[i][2]:
                use_B.append(matrix[i][3])
            else:
                use_B.append(0)
        
        # A,B가 접근 가능한 충전기 리스트를 받고
        # print(use_A)
        # print(use_B)
        E1 = -987654321
        for m in range(A):
            for n in range(A):
                if m == n:
                    # 동일한 충전기를 택하는 경우
                    E1 = max(E1, use_A[m]//2 + use_B[n]//2)
                else:
                    E1 = max(E1, use_A[m] + use_B[n])
        result += E1
        if idx == M:
            break
        dir_info_A = move_A[idx]
        dir_info_B = move_B[idx]
        Ax = Ax + dx[dir_info_A]
        Ay = Ay + dy[dir_info_A]
        Bx = Bx + dx[dir_info_B]
        By = By + dy[dir_info_B]
        idx += 1
    print(f"#{tc} {result}")

