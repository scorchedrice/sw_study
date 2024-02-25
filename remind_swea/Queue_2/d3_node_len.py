from collections import deque

def BFS(start):
    q = deque()
    now = start
    visited[now] = 1
    while True:
        for k in range(len(my_map[now])):
            if visited[my_map[now][k]] == 0:
                q.append(my_map[now][k])
                visited[my_map[now][k]] = visited[now] + 1
        if q == deque():
            return 0
        now = q.popleft()
        if now == end:
            return visited[end] -1

T=int(input())
for tc in range(1,T+1):
    island, bridge = map(int,input().split())
    my_map = [[] for _ in range(island+1)]

    for k in range(bridge):
        a, b = map(int,input().split())
        my_map[a] += [b]
        my_map[b] += [a]
        #방향성이 없기에

    start, end = map(int,input().split())
    # 시작점과 도착점

    visited = [0] * (island+1)
    print(f"#{tc} {BFS(start)}")