# 스도쿠
def qs(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    tail = list[1:]
    left = [num for num in tail if num < pivot]
    right = [num for num in tail if num >= pivot]
    return qs(left) + [pivot] + qs(right)

def transpose_matrix(total_map):
    for i in range(9):
        for j in range(9):
            if i<j:
                total_map[i][j], total_map[j][i] = total_map[j][i], total_map[i][j]
    return total_map

def check_map(total_map):
    result = 0
    for i in range(9):
        if total_map[i] == list(range(1,10)):
            result += 1
    if result == 9:
        return True
    else:
        return False

def check_block(total_map):
    my_list = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            my_list += [[total_map[i][j]] + [total_map[i][j+1]] + [total_map[i][j+2]] + [total_map[i+1][j]] + [total_map[i+1][j+1]] + [total_map[i+1][j+2]] + [total_map[i+2][j]] +  [total_map[i+2][j+1]] + [total_map[i+2][j+2]]]
    
    sort_my_list = []
    for i in range(9):
        sort_my_list += [qs(my_list[i])]
    
    result = 0
    for i in range(9):
        if sort_my_list[i] == list(range(1,10)):
            result = result + 1
    
    if result == 9:
        return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    result = []
    total_map = []
    for i in range(9):
        total_map += [list(map(int, input().split()))]

    # 행 확인
    sort_total_map = []
    for i in range(9):
        sort_total_map += [qs(total_map[i])]

    result += [check_map(sort_total_map)]

    # 박스 확인
    result += [check_block(total_map)]


    # 열 확인
    transpose_matrix(total_map)
    sort_total_map_transpose = []
    for i in range(9):
        sort_total_map_transpose += [qs(total_map[i])]

    result += [check_map(sort_total_map_transpose)]

    if result == [True, True, True]:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
