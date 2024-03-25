import sys

di = [1,-1,0,0]
dj = [0,0,1,-1]

def dfs(ci,cj,idx):
    global result
    if idx == M:
        result += 1
        return
    for dir in range(4):
        mi = ci + di[dir]
        mj = cj + dj[dir]
        if 0<=mi<N and 0<=mj<N and visited[mi][mj] == 0:
            if (mi,mj) == target[idx]:
                visited[mi][mj] = 1
                dfs(mi,mj,idx+1)
                visited[mi][mj] = 0
            elif (mi,mj) != target[idx] and (mi,mj) in target:
                continue
            else:
                visited[mi][mj] = 1
                dfs(mi,mj,idx)
                visited[mi][mj] = 0
    else: # 4방향 모두 돌아도 갈 수 없는 경우
        return
    
N, M = map(int,input().split())
matrix = []
wall_idx = []
for k in range(N):
    memory = list(map(int,input().split()))
    for m in range(N):
        if memory[m] == 1:
            wall_idx.append((k,m))
    matrix.append(memory)

target = []
for l in range(M):
    i,j = map(int,input().split())
    target.append((i-1,j-1))

result = 0
visited = [[0]*N for _ in range(N)]
for n in range(len(wall_idx)):
    wall = wall_idx[n]
    visited[wall[0]][wall[1]] = 1
    
dfs(target[0][0],target[0][1],1)
print(result)