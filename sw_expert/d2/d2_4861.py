def find_pal(my_str):
    n = len(my_str)
    for_result = 0
    for i in range(n//2):
        if my_str[i] == my_str[-(i+1)]:
            for_result += 1

        else:
            break
    if for_result == n//2:
        return True
    else:
        return False

def i_j_change(total_str):
    result = []
    for j in range(N):
        for_result = ''
        for i in range(N):
            for_result += total_str[i][j]
        result += [for_result]
    return result

T = int(input())
for tc in range(1,T+1):
    N , M = map(int, input().split())
    total_str = []
    for i in range(N):
        total_str += [input()]

    # 한 행씩 일치여부를 판단하는 과정
    for i in range(N):
        result = 0
        for cut in range(N-M+1):
            for_result = total_str[i][cut:cut+M]
            if find_pal(for_result) == True:
                print(f"#{tc} {for_result}")

    # 한 열의 일치 여부를 판단하는 과정
    total_str_change = i_j_change(total_str)
    for i in range(N):
        result = 0
        for cut in range(N-M+1):
            for_result = total_str_change[i][cut:cut+M]
            if find_pal(for_result) == True:
                print(f"#{tc} {for_result}")

