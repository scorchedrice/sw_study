from heapq import heappop, heappush

def prim(start):
    Q = []
    heappush(Q, (0,start))
    visited = [0] * (N+1)
    weight = 0
    while Q:
        cost, current = heappop(Q)
        if visited[current] == 0: # 방문한 적이 없다면
            visited[current] = 1
            weight += cost
        else:
            continue
        
        for nxt in range(N+1):
            if matrix[current][nxt] == 0 or visited[nxt] == 1:
                # 방문기록이 있거나 갈 수 없는 경우엔
                continue
            heappush(Q, (matrix[current][nxt], nxt))
    return weight

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    matrix = [[0] * (N+1) for _ in range(N+1)]
    # matrix 세팅
    # print(matrix)
    for _ in range(M):
        s,e,c = map(int,input().split())
        matrix[s][e] = c
        matrix[e][s] = c
    result = prim(0)
    print(f"#{tc} {result}")