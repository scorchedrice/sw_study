from heapq import heappush, heappop

def DIJ():
    global dist
    Q = []
    heappush(Q,(0,0)) # cost, start
    dist[0] = 0
    while Q:
        cost, now = heappop(Q)
        if cost > dist[now]:
            continue
        for k in matrix[now]:
            # k[0] : month, k[1] : cost
            pivot = k[1] + cost
            if dist[k[0]] > pivot:
                dist[k[0]] = pivot
                heappush(Q,(pivot,k[0]))

T = int(input())
for tc in range(1,T+1):
    INF = 987654321
    dist = [INF] * 13
    dist[0] = 0
    day,month,month3,year = map(int,input().split())
    plan = list(map(int,input().split()))
    matrix = [[] for _ in range(13)]
    for k in range(0,12):
        if k == 0:
            matrix[k].append((12,year)) # 12월, 연간권
        matrix[k].append((k+1,day*plan[k]))
        matrix[k].append((k+1,month))
        if k+3 <= 12:
            matrix[k].append((k+3,month3))
        else:
            matrix[k].append((12,month3))
    # print(matrix)
    DIJ()
    print(f"#{tc} {dist[12]}")