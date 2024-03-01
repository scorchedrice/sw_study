def dfs(n,lst):
    if n >= 2:
        if sum(lst) < N:
            total.append(lst)
        return

    for i in range(1,N-1):
        dfs(n+1, lst+[i])

# T = int(input())
# for tc in range(1,T+1):
N, M = map(int,input().split())
matrix = []
for _ in range(N):
    matrix.append(list(input()))
cnt_W = 0
cnt_B = 0
cnt_R = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'W':
            cnt_W += 1
        elif matrix[i][j] == 'B':
            cnt_B += 1
        else:
            cnt_R += 1

total = []
dfs(0,[])

# W범위 : 0이상 result[0] 미만
# B범위 : W 마지막 + 1 부터 그 i + result[1]
# R범위 : 나머지

# White_end = result[0]
# Blue_start = result[0]
# Blue_end = result[1]
# Red_start = result[1]
# Red_end = N
my_result = 987654321
for result in total:
    cnt_paint = 0
    for i_white in range(0,result[0]):
        for j_white in range(M):
            if matrix[i_white][j_white] != 'W':
                cnt_paint += 1
    for i_blue in range(result[0], result[0] + result[1]):
        for j_blue in range(M):
            if matrix[i_blue][j_blue] != 'B':
                cnt_paint += 1
    for i_red in range(result[0] + result[1], N):
        for j_red in range(M):
            if matrix[i_red][j_red] != 'R':
                cnt_paint += 1
    if cnt_paint < my_result:
        my_result = cnt_paint
print(my_result)