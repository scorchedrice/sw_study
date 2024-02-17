N, M = map(int,input().split())

map_matrix = [[987654321] * (N+1) for _ in range(N+1)] # 정답지가 될 matrix 작성
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            map_matrix[i][j] = 0
# 도착지와 출발지가 같은 경우 이를 0으로 변경
for _ in range(M):
    from_a, to_b = map(int, input().split())
    map_matrix[from_a][to_b] = 1
    map_matrix[to_b][from_a] = 1

X, K = map(int, input().split())
# K가 우선 방문, 이후 X 방문

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            map_matrix[a][b] = min(map_matrix[a][b], map_matrix[a][k] + map_matrix[k][b])

result = map_matrix[1][K] + map_matrix[K][X]
if result >= 987654321:
    print('Floyd')
    print('-1')
else:
    print('Floyd')
    print(result)