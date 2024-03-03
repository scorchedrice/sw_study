def dfs(n,lst):
    if n >= 2:
        if sum(lst) < N:
            total.append(lst)
        return

    for i in range(1,N-1):
        dfs(n+1, lst+[i])

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(input()))
    total = []
    dfs(0,[])
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
    print(f"#{tc} {my_result}")