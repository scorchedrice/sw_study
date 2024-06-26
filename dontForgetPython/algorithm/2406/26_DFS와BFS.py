from collections import deque
from copy import deepcopy

island, bridge, first = map(int,input().split())

matrix = [[] for _ in range(island + 1)]
DFSvisited = [0 for _ in range(island + 1)]
DFSvisited[first] = 1
BFSvisited = deepcopy(DFSvisited)

for _ in range(1,bridge+1):
    start, end = map(int,input().split())
    matrix[start] += [end]
    matrix[end] += [start]

for _ in range(1,island+1):
    matrix[_] = sorted(matrix[_])

# DFS
recordDFS = []
stack = []
stack += [first]
now = deepcopy(first)
recordDFS = [now]
DFSvisited[now] = 1
while True:
    for target in matrix[now]:
        if DFSvisited[target] == 0:
            # 방문 기록이 없다면
            stack += [now]
            # 스택에 이를 추가하고
            now = target
            recordDFS += [now]
            # 해당 위치로 이동한 뒤
            DFSvisited[now] = 1
            # 방문 기록을 남긴다.
            break
    else:
        if stack == []:
            # 스택이 비어있다면 중단해야한다.
            break
        else:
            # for문에 걸리지 않는 경우(갈곳이 없으면)
            now = stack.pop()
            # 한 단계 뒤로 간다.

print(*recordDFS)

# BFS
now = deepcopy(first)
BFSvisited[now] = 1
recordBFS = []
que = deque()
que.append(now)
while True:
    for target in matrix[now]:
        if BFSvisited[target] == 0:
            # 타겟을 방문한적이 없다면
            que.append(target)
            BFSvisited[target] = 1
    else:
        if que == deque():
            break
        else:
            now = que.popleft()
            recordBFS += [now]

print(*recordBFS)
