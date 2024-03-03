'''
n x n size
기지국에 커버되지 "않는" 집의 수를 찾고자 한다
'''
'''
집이 위치한 원소는 H, 기지국이 위치한 원소는 A, B, C
A는 주변 1칸, B는 주변 2칸, C는 주변 3칸
X는 빈 공간
'''
def check_point(matrix):
    global cnt
    result = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 'X' and matrix[i][j] != 'H':
                result += [(matrix[i][j], i, j)]
            elif matrix[i][j] == 'H':
                cnt += 1
    return result

def change_home(matrix, check):
    global cnt
    for info in check:
        if info[0] == 'A':
           my_range = 1
        elif info[0] == 'B':
           my_range = 2
        else:
            my_range = 3
        di = [-1,1,0,0] # 상하좌우
        dj = [0,0,-1,1]
        for dir in range(4):
            for k in range(1,my_range+1):
                move_i = info[1] + k*di[dir]
                move_j = info[2] + k*dj[dir]
                if 0<=move_i<=N-1 and 0<=move_j<=N-1:
                    if matrix[move_i][move_j] == 'H':
                        cnt -= 1
                        matrix[move_i][move_j] = 'X'
    

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(input()))
    cnt = 0
    check = check_point(matrix)
    change_home(matrix, check)
    print(f"#{tc} {cnt}")