# 모든 방 번호는 다르므로 굳이 stack을 활용할 필요 없음.
di = [-1,1,0,0]
dj = [0,0,-1,1]
def move(si,sj):
    ci, cj = si, sj
    cnt = 1
    room_num = matrix[si][sj]
    while True:
        for dir in range(4):
            mi = ci + di[dir]
            mj = cj + dj[dir]
            if 0<=mi<N and 0<=mj<N and matrix[mi][mj] - matrix[ci][cj] == 1:
                ci = mi
                cj = mj
                cnt += 1
                break
        else:
            result.append((cnt,-1*room_num))
            return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int,input().split())))

    result = []

    
    for i in range(N):
        for j in range(N):
            move(i,j)
    
    result.sort()
    
    final_result = result[-1]
    mx_room = final_result[1] * (-1)
    mx_cnt = final_result[0]
    print(f"#{tc} {mx_room} {mx_cnt}")