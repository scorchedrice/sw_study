'''
A~E (ABCDE ... idx 4까지)
일방통행
'''
import heapq
def Dij():
    Q = []
    heapq.heappush(Q, (0,0))
    # idx 0 : node, idx 1 : cost
    while True:
        if Q == []:
            return dist[N]
        node, d = heapq.heappop(Q)
        # 이전 연산에서 최단거리를 구했다면
        if d > dist[node]:
            continue
        
        for near_info in matrix[node]:
            next_node = near_info[0]
            next_d = near_info[1]
            pivot = d + next_d
            # 가성비 따지기
            if pivot < dist[next_node]:
                # 경유가 더 저렴하다면
                dist[next_node] = pivot
                heapq.heappush(Q, (next_node, next_d))



T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split())
    # last, road
    matrix = [[] for _ in range(N+1)]
    # 0(start) 포함
    INF = 987654321
    dist = [INF] * (N+1)
    dist[0] = 0
    # 시작지점이 정해져있으므로
    for _ in range(E):
        s,e,c = map(int,input().split())
        matrix[s] += [(e,c)]
    print(f"#{tc} {Dij()}")
    