'''
출발은 0,0 으로 고정
인접지역 이동시 1 소모, 높이 차만큼 + 소모
'''
from heapq import heappop, heappush
di = [0,0,1,-1]
dj = [1,-1,0,0]
# delta 활용한 인접리스트 생성
def setting_table():
    for i in range(N):
        for j in range(N):
            ci = i
            cj = j
            for dir in range(4):
                mi = ci + di[dir]
                mj = cj + dj[dir]
                if abs(mi-ci) + abs(mj-cj) == 1 and 0<=mi<N and 0<=mj<N:
                    # 한칸 차이나고 인덱스를 만족하는 경우
                    if matrix[mi][mj] > matrix[ci][cj]:
                        table[i][j].append((mi,mj,matrix[mi][mj]-matrix[ci][cj]+1))
                    else:
                        table[i][j].append((mi,mj,1))

def Dij(si, sj):
    global fuel
    # start i and start j
    Q = []
    heappush(Q, (si,sj,0)) # start i, start j, cost
    fuel[si][sj] = 0 # 시작지점 거리정보 초기화
    
    while Q:
        ci, cj, f = heappop(Q)
        if f > fuel[ci][cj]: # 이미 짧은 거리가 연산되었으니
            continue
        for near in table[ci][cj]:
            # print(near)
            near_i = near[0]
            near_j = near[1]
            near_fuel = near[2]
            pivot = near_fuel + f
            if pivot < fuel[near_i][near_j]:
                fuel[near_i][near_j] = pivot
                heappush(Q,(near_i, near_j, pivot))
                # print(fuel)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    table = [[[] for _ in range(N)] for _ in range(N)]
    # 매트릭스를 구성하는 과정
    for _ in range(N):
        matrix.append(list(map(int,input().split())))
    # print(matrix)
    setting_table()
    # print(table)
    INF = 1e9
    fuel = [[INF for _ in range(N)] for _ in range(N)]
    Dij(0,0)
    print(f"#{tc} {fuel[N-1][N-1]}")