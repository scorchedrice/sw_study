N, K = map(int,input().split())
lst = [(0,0)]
for _ in range(N):
    lst.append(tuple(map(int,input().split())))
matrix = [[0]*(K+1) for _ in range(N+1)]
# 여기까지 물건의 리스트를 받고, 매트릭스를 생성하는 과정

for i in range(1,N+1):
    for j in range(1,K+1):
        w = lst[i][0] # 확인할 물건의 무게
        v = lst[i][1] # 확인할 물건의 가치
        if j >= w: # 들어갈 수 있다면 값을 비교한다.
            matrix[i][j] = max(matrix[i-1][j], v + matrix[i-1][j-w])
        else: # 들어갈 수 없다면, 윗 행의 값을 가져온다.
            matrix[i][j] = matrix[i-1][j]

print(matrix[N][K])