def dfs(n,cost):
    global mn
    if n == N:
        if mn > cost:
            mn = cost
        return
    if cost > mn:
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1,cost+matrix[n][i])
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int,input().split())))
    visited = [0] * (N)
    mn = 987654321
    dfs(0,0)
    print(f"#{tc} {mn}")