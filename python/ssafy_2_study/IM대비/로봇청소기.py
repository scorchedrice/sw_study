def find_dust(now_i, now_j):
    candidate_R = []
    candidate_L = []
    candidate_U = []
    candidate_D = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                if j != now_j:
                    tan_theta = (i-now_i)/(j-now_j)
                elif j == now_j:
                    if i < now_i:
                        candidate_U.append(((now_i-i)**2 + (now_j-j)**2,i,j))
                        continue
                    else:
                        candidate_D.append(((now_i-i)**2 + (now_j-j)**2,i,j))
                        continue
                '''
                tan_theta범위에 따른 탐색 영역
                1이상 : U
                -1이상1이하 : R or L
                -1이하 : D
                # 방사형 탐색으로, 45도라인에선 겹칠 수 있기에, 이상 이하로 중복 추가할 수 있음.
                '''
                if abs(tan_theta) >= 1:
                    if i < now_i: # 먼지가 더 위에 있으면
                        candidate_U.append(((now_i-i)**2 + (now_j-j)**2,i, j))
                    elif i > now_i:
                        candidate_D.append(((now_i-i)**2 + (now_j-j)**2,i, j))
                if -1<=tan_theta<=1:
                    if j > now_j: # 먼지가 더 오른쪽에 있으면
                        candidate_R.append(((now_i-i)**2 + (now_j-j)**2,i,j))
                    elif j < now_j:
                        candidate_L.append(((now_i-i)**2 + (now_j-j)**2,i,j))
    candidate_U.sort()
    candidate_D.sort()
    candidate_R.sort()
    candidate_L.sort()
    return candidate_U, candidate_D, candidate_L, candidate_R

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int,input().split())))
    work = list(input())
    work_time = len(work)

    cnt = 0
    now_i = 0
    now_j = 0
    dir_info = ['U', 'D', 'L', 'R']
    while True:
        dir_data = work[cnt]
        cnt += 1
        if dir_data == 'R':
            target = find_dust(now_i, now_j)[3]
        elif dir_data == 'L':
            target = find_dust(now_i, now_j)[2]
        elif dir_data == 'D':
            target = find_dust(now_i, now_j)[1]
        else:
            target = find_dust(now_i, now_j)[0]
        
        if target != []:
            matrix[target[0][1]][target[0][2]] = 0
            now_i = target[0][1]
            now_j = target[0][2]
        print(matrix)
        if cnt == work_time:
            break

    print(f"#{tc}")
    for _ in range(N):
        print(*matrix[_])