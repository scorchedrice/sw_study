def check_i(total_map):
    for i in range(N):
        mok_cnt = 0
        for j in range(N):
            if total_map[i][j] == 'o': # 돌이 존재한다면
                mok_cnt += 1 # cnt를 1 더하고
                if mok_cnt == 5: # 그 값이 5라면 True
                    return True
                else:
                    continue # 아니면 계속 진행
            else:
                mok_cnt = 0 # .을 발견한 경우 cnt 초기화
    return False

def check_j(total_map):
    for j in range(N):
        mok_cnt = 0
        for i in range(N):
            if total_map[i][j] == 'o': # 돌이 존재한다면
                mok_cnt += 1 # cnt를 1 더하고
                if mok_cnt == 5: # 그 값이 5라면 True
                    return True
                else:
                    continue # 아니면 계속 진행
            else:
                mok_cnt = 0 # .을 발견한 경우 cnt 초기화
    return False
            
def check_diag_positive(total_map):
    for i in range(N-4):
        for j in range(N-4):
            if [total_map[i][j], total_map[i+1][j+1], total_map[i+2][j+2], total_map[i+3][j+3], total_map[i+4][j+4]] == ['o','o','o','o','o']:
                return True
    return False

def check_diag_negative(total_map):
    for i in range(N-4):
        for j in range(N-4):
            if [total_map[i][j+4], total_map[i+1][j+3], total_map[i+2][j+2], total_map[i+3][j+1], total_map[i+4][j]] == ['o','o','o','o','o']:
                return True
    return False

def this_is_result(total_map):
    if check_i(total_map) == True or check_j(total_map) == True or check_diag_negative(total_map) == True or check_diag_positive(total_map) == True:
        return 'YES'
    else:
        return 'NO'

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    total_map = []
    for i in range(N):
        total_map += [list(input())]

    print(f"#{tc} {this_is_result(total_map)}")
