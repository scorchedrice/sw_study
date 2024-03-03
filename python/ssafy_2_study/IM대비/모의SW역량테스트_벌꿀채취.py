T = int(input())
for tc in range(1,T+1):
    N, M, C = map(int,input().split())
    # N 은 matrix size
    # M 은 일꾼이 작업할 공간 크기
    # C 는 일꾼이 채취할 수 있는 꿀의 양
    def dfs(n,cost,sm,ci,cj):
        global mx
        if sm > C:
            return
        if n == M:
            mx = max(mx, cost)
            return    
        dfs(n+1, cost + matrix[ci][cj+n]**2, sm + matrix[ci][cj + n], ci, cj)
        dfs(n+1, cost, sm, ci, cj)

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int,input().split())))

    result = 0
    for i1 in range(N):
        for j1 in range(N-M+1):
            # 일꾼1이 작업 시작할 위치
            for i2 in range(N):
                mx = 0
                dfs(0,0,0,i1,j1)
                mx_1 = mx
                if i2 == i1:
                    k = j1 + M
                else:
                    k = 0
                for j2 in range(k, N-M+1):
                    mx = 0
                    dfs(0,0,0,i2,j2)
                    mx_2 = mx
                    if result < mx_1 + mx_2:
                        result = mx_1 + mx_2
    print(f"#{tc} {result}")