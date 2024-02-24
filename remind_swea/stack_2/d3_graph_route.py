def DFS(start):
    stack = [start]
    visited = [0] * (island+1)
    visited[start] = 1
    now = start

    while True:
        for k in range(len(map_info[now])):
            if visited[map_info[now][k]] == 0: # 해당 위치가 방문한 적이 없다면
                now = map_info[now][k]
                visited[now] = 1
                stack += [now]
                break
        else:
            if stack == []:
                return visited[end]
            else:
                now = stack.pop()

T = int(input())
for tc in range(1,T+1):
    island, bridge = map(int,input().split())
    map_info = [[] for _ in range(island + 1)]
    for k in range(bridge):
        download_island, download_bridge = map(int,input().split())
        map_info[download_island] += [download_bridge]

    start, end = map(int,input().split())

    print(f"#{tc} {DFS(start)}")