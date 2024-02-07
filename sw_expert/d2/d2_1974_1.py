# 사이즈는 9, (9*9)
def check_i_sum(total_map):
    for i in range(9):
        my_result = sorted(total_map[i])
        if my_result != [1,2,3,4,5,6,7,8,9]:
            return False
        else:
            continue
    return True

def check_j_sum(total_map):
    new_total_map = []
    for j in range(9):
        for_ij_change = []
        for k in range(9):
            for_ij_change += [total_map[k][j]]
        new_total_map += [for_ij_change]
    
    for i in range(9):
        my_result = sorted(new_total_map[i])
        if my_result != [1,2,3,4,5,6,7,8,9]:
            return False
        else:
            continue
    return True

def check_block(total_map):
    check_start_index = [0,3,6]
    new_total_map = []

    for j in check_start_index: 
        for i in check_start_index:
            for_make_block_list = []
            for_make_block_list += [total_map[i][j],total_map[i][j+1],total_map[i][j+2]]
            for_make_block_list += [total_map[i+1][j],total_map[i+1][j+1],total_map[i+1][j+2]]
            for_make_block_list += [total_map[i+2][j],total_map[i+2][j+1],total_map[i+2][j+2]]
            new_total_map += [for_make_block_list]

    for m in range(9):
        my_result = sorted(new_total_map[m])
        if my_result != [1,2,3,4,5,6,7,8,9]:
            return False
        else:
            continue
    return True

def this_is_result(total_map):
    result_list = [check_i_sum(total_map), check_j_sum(total_map), check_block(total_map)]
    if result_list == [True, True, True]:
        return 1
    else:
        return False

total_map = []
for size in range(9):
    total_map += [list(map(int, input().split()))]

print(this_is_result(total_map))