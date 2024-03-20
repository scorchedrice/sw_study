'''
oper = ['+1','-1','*2','-10']
'''
from collections import deque

T = int(input())
for tc in range(1,T+1):
    origin, target = map(int,input().split())

    def bfs(origin, target):
        Q = deque()
        Q.append(origin)
        visited = [0] * 1000001
        visited[origin] = 1
        while Q:
            t = Q.popleft()
            if t == target:
                return visited[t]-1
            # t에 인접한 w, 방문한 적이 없으면
            if t-10 > 0 and visited[t-10] == 0:
                Q.append(t-10)
                visited[t-10] = visited[t] + 1
            if 0 < t-1 and visited[t-1] == 0:
                Q.append(t-1)
                visited[t-1] = visited[t] + 1
            if t+1<= 1000000 and visited[t+1] ==0:
                Q.append(t+1)
                visited[t+1] = visited[t] + 1
            if t*2 <= 1000000 and visited[t*2] == 0:
                Q.append(t*2)
                visited[t*2] = visited[t] + 1
        return visited
    ans = bfs(origin,target)
    print(f"#{tc} {ans}")