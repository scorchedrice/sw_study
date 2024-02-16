T = int(input())
for tc in range(1,T+1):

    V, E = map(int, input().split())
    # V는 노드의 수, E는 간선의 수
    mapdata = []
    for _ in range(E):
        mapdata += [list(map(int, input().split()))]
    realmap = [[] for _ in range(V+1)]
    for k in mapdata:
        realmap[k[0]] += [k[1]]
        realmap[k[1]] += [k[0]]

    start, end = map(int, input().split())

    current = start
    Q = []
    visited = [987654321] * (V+1)
    visited[current] = 1
    while True:
        for k in realmap[current]:
            if visited[k] == 987654321:
                Q += [k]
                visited[k] = visited[current] + 1
            else:
                continue
        if Q == []:
            break
        current = Q.pop(0)
        if current == end:
            break
    if visited[end] == 987654321:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} {visited[end]-1}")