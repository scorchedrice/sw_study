from collections import deque
# 연결 리스트를 활용한 트리구조

T = int(input())
for tc in range(1,T+1):
    bridge, subtree_node = map(int,input().split())
    tree = [[] for _ in range(bridge + 2)]
    info = list(map(int,input().split()))
    for i in range(0,len(info),2):
        tree[info[i]] += [info[i+1]]

    now = subtree_node
    num = 1
    visited = [0] * (bridge+2)
    visited[now] = num
    q = deque()
    while True:
        for i in range(len(tree[now])):
            q.append(tree[now][i])
            visited[tree[now][i]] = visited[now] + 1
        if q == deque():
            break
        now = q.popleft()

    result = 0
    for i in range(1,bridge+2):
        if visited[i] != 0:
            result += 1
    print(f"#{tc} {result}")