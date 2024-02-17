# 1은0, 0은1로 바뀌는 연산을 토글이라고 한다
# k초가 되는 순간 i+j가 k와 같거나 k의 배수가 되는 영역은 토글된다.
# 단 M이 k의 배수인 경우 M초에는 (2)를 따르는 대신 전체가 토글된다.
def my_toggle(matrix,i,j):
    if matrix[i][j] == 1:
        matrix[i][j] = 0
    elif matrix[i][j] == 0:
        matrix[i][j] = 1
    return

def all_toggle(matrix):
    for i in range(1,N+1):
        for j in range(1,N+1):
            my_toggle(matrix,i,j)
    return

def count_one(matrix):
    result = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if matrix[i][j] == 1:
                result += 1
    return result

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    my_time_list = list(range(1,M+1))
    matrix = [[9]*(N+1)]
    for _ in range(N):
        matrix += [[9] + list(map(int,input().split()))]

    for k in my_time_list:
        if M%k == 0: # M이 k의 배수인경우
            all_toggle(matrix)
        else:
            for i in range(1,N+1):
                for j in range(1,N+1):
                    if (i+j)%k == 0:
                        my_toggle(matrix,i,j)

    print(f"#{tc} {count_one(matrix)}")


