from collections import deque
def bfs(start):
    visited = [0] * 101
    Q = deque()
    Q.append(start)
    visited[start] = 1
    last_num = 0
    while Q:
        now = Q.popleft()
        for i in range(len(matrix[now])):
            nxt = matrix[now][i]
            if visited[nxt] == 0:
                visited[nxt] = visited[now] + 1
                last_num = visited[now] + 1
                Q.append(nxt)
    last_lst = []
    for l in range(101):
        if last_num ==  visited[l]:
            last_lst.append(l)
    return max(last_lst)
T = 10
for tc in range(1,T+1):
    N, start = map(int,input().split())
    lst = list(map(int,input().split()))
    matrix = [set() for _ in range(101)]
    for k in range(0,N,2):
        a = lst[k]
        b = lst[k+1]
        matrix[a].add(b)
    for l in range(101):
        matrix[l] = list(matrix[l])
    
    result = bfs(start)
    print(f"#{tc} {result}")
    
        
            