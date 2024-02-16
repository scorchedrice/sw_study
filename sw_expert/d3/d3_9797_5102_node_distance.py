# V개의 노드 (섬), E개의 간선 (다리)
# 출발 지점과 도착 지점을 줄테니, 최단 거리를 구하라
# 노드는 1번부터 존재하며, 간선으로 연결되지 않은 경우 존재
# V : 5이상 51 미만, E : 4이상 1001 미만의 정수
'''
시작 지점과 도착 지점이 정해져있으므로
다익스트라 최단경로 알고리즘 활용 가능.
'''
import heapq

def Dij(start):
    Q = []
    heapq.heappush(Q, (start,0))
    # Q에 (위치, 카운트)를 push
    distance[start] = 0
    # 출발할 지점의 값을 0으로 바꾼다.
    # 이는 출발지점에서 출발지점까지 가야하는 거리가 0이기 때문
    
    while Q != []:
        # == Q가 비면 멈춘다.
        current, cost = heapq.heappop(Q)
        # Q 맨앞을 pop한다.
        if distance[current] < cost:
            continue
        # 현재 distance값이 cost보다 낮다면 (즉, 이전에 가공된 적이 있다면) continue

        for i in mapinfo[current]:
            new_cost = cost + i[1]
            # new_cost는 현 위치를 경유하여 가는 거리를 의미한다.
            if new_cost<distance[i[0]]:
                # 만약 위에서 기록한 cost (direct)보다 가성비가 좋다면
                distance[i[0]] = new_cost
                # 거쳐가는 값을 재할당한다.
                heapq.heappush(Q, (i[0], new_cost))
                # 새로운 값을 Q에 push한다.
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    mapinfo = [[] for _ in range(V+1)] # map에 대한 정보를 담을 리스트
    input_mapinfo = [list(map(int, input().split())) for _ in range(E)]
    # input되는 map data
    for k in input_mapinfo:
        mapinfo[k[0]] += [(k[1],1)]
        mapinfo[k[1]] += [(k[0],1)]
    # 해당 데이터를 기반으로 mapinfo를 완성한다.
    # 해당 위치로 이동 할 때 1을 추가할 것이므로 1이 함께 있는 tuple 활용

    distance = [987654321] * (V+1)
    # 일단 987654321으로 이뤄진 리스트를 만든다. (무한대의 개념)
    # 이 값들은 방문 가능하다면 수정될 값들이고, 방문이 불가능하다면 값이 바뀌지 않음
    # 즉, 이후 이 값을 확인했을 때 방문 가능여부를 판단할 수 있다는 것.

    start, end = map(int, input().split())
    Dij(start)
    # 시작 지점과 도착 지점 데이터를 입력받고 정의한 다익스트라 알고리즘을 실행한다.


    if distance[end] == 987654321:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} {distance[end]}")
