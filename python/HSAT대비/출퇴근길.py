'''
# 해설 참고했음. 역방향 인접 리스트의 필요성

문제 조건에서 출근길의 경우 집을 수차례 들려도,
    퇴근길에 회사를 수차례 들려도 가능한 경우의 수로 취급한다고 명시해뒀음.
따라서 집에서 어딘가를 떠돌다가 다시 집을 간 후 출근하는 경우 또한 고려해야한다는 이야기.

역뱡항 인접 리스트가 왜 필요한가?
- 출근하는 경우를 고려해보면, 집 주변을 맴돌다 출근하는 경우에, 이 경우를 따져줘야 한다.
    즉, 딴길로 갔을 때, 과연 그 노드에서 다시 집으로 돌아갈 수 있는지 확인하는 과정이 필요하다.
- 역방향 리스트를 구성했을 때, 해당 노드에서 목적지를 갈 수 있다는 것은,
    목적지에서 해당 노드로 이동 가능한다는 것을 의미한다.
'''
from collections import deque

def bfs(start,matrix,v):
    Q = deque()
    Q.append(start)
    v[start] = 1
    while Q:
        now = Q.popleft()
        for nxt in matrix[now]:
            if v[nxt] == 1:
                continue
            else:
                v[nxt] = 1
                Q.append(nxt)

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
graph_re = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph_re[end].append(start)
S, T = map(int,input().split())

fromS=[0]*(n+1)
fromS[T]=1          # S->T 1로 미리 세팅
bfs(S,graph,fromS)

fromT=[0]*(n+1)
fromT[S]=1          # T->S 1로 미리 세팅

bfs(T,graph,fromT)

toS=[0]*(n+1)
bfs(S,graph_re,toS)

toT=[0]*(n+1)
bfs(T,graph_re,toT)
answer=0

ans = 0
for k in range(1,n+1):
    if k == S or k == T:
        continue
    else:
        if fromT[k] == 1 and fromS[k] == 1 and toS[k] == 1 and toT[k] == 1:
            ans += 1
print(ans)