'''
4*4 격자판, 각 격자칸에는 0부터 9사이의 숫자가 적혀있음 (0이상9이하)
격자판 임의의 위치에서 시작한다. 동서남북 네방향으로 인접한 격자로 총 여섯번 이동(델타, BFS, DFS 중 하나?)
각 칸에 적혀있는 숫자를 차례대로 이어붙히면 7자리의 수 (ok)
한번 거쳤던 격자칸 다시 거쳐도 된다. (visited 불필요)
단 격자판을 벗어나는 이동은 제한된다.
'''
di = [-1,1,0,0] # 상하좌우
dj = [0,0,-1,1]

def dfs(i,j,n,lst):
    if n == 6:
        ans.append(''.join(lst))
        return
    
    for dir in range(4):
        if 0<=i+di[dir]<=3 and 0<=j+dj[dir]<=3:
            i = i+di[dir]
            j = j+dj[dir]
            dfs(i,j,n+1,lst+[matrix[i][j]])
            i = i-di[dir]
            j = j-dj[dir]

# 일곱자리 수 만들 것! (이동 6번)
# 시작지점은 1부터 시작한다. (1이 존재하는 위치 찾고, 그에 해당하는 재귀 실행)
T = int(input())
for tc in range(1,T+1):
    matrix = []
    for _ in range(4):
        matrix += [list(input().split())]
    start_list = []
    
    
    ans = []
    for i in range(4):
        for j in range(4):
            dfs(i,j,0,[matrix[i][j]])
    print(f"#{tc} {len(set(ans))}")