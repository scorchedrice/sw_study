di = [-1,1,0,0] # 상하좌우
dj = [0,0,-1,1]
def dfs(si,sj,lst):
    global result
    if len(lst) == 7:
        result.add(lst)
        return
    ci = si
    cj = sj
    for dir in range(4):
        mi = ci + di[dir]
        mj = cj + dj[dir]
        if 0<=mi<=3 and 0<=mj<=3:
            dfs(mi,mj,lst+matrix[mi][mj])
       
    

T = int(input())
for tc in range(1,T+1):
    matrix = []
    for _ in range(4):
        matrix.append(list(input().split()))
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,matrix[i][j])
    print(f"#{tc} {len(result)}")