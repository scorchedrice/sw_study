# 32-2 testcase 부터 시간초과
from collections import deque

def bfs(start,end):
    visited = [0] * (N+1)
    Q = deque()
    Q.append(start)
    lst = []
    visited[start] = 1
    visited[end] = 1
    while Q:
        now = Q.popleft()
        lst.append(now)
        for near in range(len(matrix[now])):
            nxt_node = matrix[now][near]
            if visited[nxt_node] == 0:
                if check(nxt_node,end,lst) == True:
                    visited[nxt_node] = 1
                    Q.append(nxt_node)
    return visited

def check(start,target,lst):
    visited = [0] * (N+1)
    visited[start] = 1
    Q = deque()
    Q.append(start)
    while Q:
        now = Q.popleft()
        if now in lst:
            return True
        if now == target:
            return True
        for near in range(len(matrix[now])):
            nxt_node = matrix[now][near]
            if visited[nxt_node] == 0:
                visited[nxt_node] = 1
                Q.append(nxt_node)
    return False

N, M = map(int,input().split())
matrix = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int,input().split())
    matrix[start].append(end)
home, company = map(int,input().split())
a = bfs(home,company)
b = bfs(company,home)
cnt = 0
for k in range(1,N+1):
    if k == home or k == company:
        continue
    else:
        if a[k] == 1 and b[k] == 1:
            # print(k)
            cnt += 1
print(cnt)