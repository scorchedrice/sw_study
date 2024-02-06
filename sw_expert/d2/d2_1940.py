# 값 입력에 활용할 함수 정의
def degree_270(list, N):
    result = []
    for j in range(N-1,-1,-1):
        one_line = []
        for k in range(0,N):
            one_line.append(list[k][j])
        result.append(one_line)
    return result

def degree_180(list, N):
    result = []
    for j in range(N-1,-1,-1):
        one_line = []
        for k in range(N-1,-1,-1):
            one_line.append(list[j][k])
        result.append(one_line)
    return result

def degree_90(list, N):
    result = []
    for j in range(0,N):
        one_line = []
        for k in range(N-1,-1,-1):
            one_line.append(list[k][j])
        result.append(one_line)
    return result

def change_matrix(list, N):
    result = []
    for j in range(0,N):
        one_line = ''
        for k in range(0,N):
            one_line += str(list[j][k])
        result.append(int(one_line))
    return result
# 입력 값은 아래의 code부터 받는다.

T = int(input())
for tc in range(0,T):
    N = int(input())
    matrix_info = []
    for size in range(0,N):
        matrix_info.append(list(map(int, input().split())))
    matrix_90 = change_matrix(degree_90(matrix_info, N),N)
    matrix_180 = change_matrix(degree_180(matrix_info, N),N)
    matrix_270 = change_matrix(degree_270(matrix_info, N),N)

    
