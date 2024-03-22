'''
다익스트라 활용 가능할 것 같음
- 1월 이용금액을 0node에서 1node로 갈 때 사용하는 비용으로 취급한다.
- 즉, 이를 활용해 12node까지 갈 때의 최소 비용을 구하는 방식으로 진행하면 된다.
    - 연 회원권은 day, month, 3month를 활용한 다익스트라 결과와 이를 비교.
'''
from heapq import heappush, heappop
def DIJ(start):
    Q = []
    INF = 987654321
    dist = [INF] * 13
    heappush(Q,(0,start))
    dist[start] = 0
    while Q:
        cost, now = heappop(Q)
        if cost > dist[now]:
            continue
        for k in range(len(matrix[now])):
            nxt_cost, nxt_month = matrix[now][k]
            pivot = nxt_cost + cost
            if pivot < dist[nxt_month]:
                dist[nxt_month] = pivot
                heappush(Q,(pivot,nxt_month))
    return dist

T = int(input())
for tc in range(1,T+1):
    day,month,month_3,year = map(int,input().split())
    lst = list(map(int,input().split()))
    matrix = [[] for _ in range(13)]
    for k in range(12):
        if lst[k] == 0:
            matrix[k].append((0,k+1))
            continue
        else:
            matrix[k].append((day * lst[k], k+1))
            matrix[k].append((month, k+1))
            if k+3 > 12:
                matrix[k].append((month_3, 12))
            elif k+3 <= 12:
                matrix[k].append((month_3, k+3))
    
    result = DIJ(0)
    print(f"#{tc} {result[-1]}")