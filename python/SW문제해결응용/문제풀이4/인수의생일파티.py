import heapq
from copy import deepcopy

def dijkstra(start):
    Q = []
    heapq.heappush(Q,(0,start)) # 우선 순위 큐 push
    dist[start] = 0
    while True:
        if Q == []:
            break
        d, current = heapq.heappop(Q) # 우선 순위 큐 pop
        if dist[current] < d:
            continue # 이미 가공된 것이라면 (d보다 작을 테니) 무시
        for i in matrix[current]:
            new_cost = d+i[1]
            # 거쳐가는 비용 계산 과정
            if new_cost < dist[i[0]]:
                # 거쳐가는 것이 더 저렴하다면
                dist[i[0]] = new_cost
                heapq.heappush(Q,(new_cost, i[0]))

T = int(input())
for tc in range(1,T+1):
    n, m, x = map(int,input().split())
    INF = 987654321
    dist = [INF] * (n+1)
    matrix = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, cost = map(int,input().split())
        matrix[a] += [(b,cost)]
    
    tmp = deepcopy(dist)
    dijkstra(x)
    insu_info = deepcopy(dist) # 인수 집에서 다른 집 까지의 거리 정보
    dist = deepcopy(tmp)

    mx = -1
    for i in range(1,n+1):
        dijkstra(i)
        a = dist[x]
        b = insu_info[i]
        if a+b > mx:
            mx = a+b
        dist = deepcopy(tmp)
    print(f"#{tc} {mx}")



