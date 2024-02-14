def return_result(matrix):
    result = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                current_i, current_j = i, j
                x_len = 1
                y_len = 1
                while True: # 우측으로 이동하며 가로길이 측정
                    if 0<=current_i+1<=N-1 and matrix[current_i+1][current_j] == 1:
                        # index조건을 만족하면서 우측으로 이동 가능할 때
                        matrix[current_i][current_j] = 0
                        current_i += 1
                        x_len += 1
                    else:
                        break
                current_i = i
                current_j = j
                while True:
                    if 0<=current_j+1<=N-1 and matrix[current_i][current_j+1] == 1:
                        matrix[current_i][current_j] = 0
                        current_j += 1
                        y_len += 1
                    else:
                        break
                result += [x_len * y_len]
    return max(result)


T = int(input())
for tc in range(1,T+1):

    N = int(input())
    matrix = []
    for _ in range(N):
        matrix += [list(map(int, input().split()))]

    print(f"#{tc} {return_result(matrix)}")