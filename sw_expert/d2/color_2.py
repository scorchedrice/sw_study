# T = int(input())
# for tc in range(1,T+1):
def check_purple_len(paper):
    result = []
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                current_i = i
                current_j = j
                x_len = 1
                y_len = 1
                while True:
                    if current_i + 1 < 10 and paper[current_i + 1][current_j] == 3:
                        x_len += 1
                        paper[current_i][current_j] = 4
                        current_i += 1
                    else:
                        break
                while True:
                    if current_j + 1 < 10 and paper[current_i][current_j + 1] == 3:
                        y_len += 1
                        paper[current_i][current_j] = 4
                        current_j += 1
                    else:
                        break
                result += [2*x_len + 2*y_len]
    return result


N = int(input())
paper = [[0]*10 for _ in range(10)]

record = []
for painting in range(N):
    start_i, start_j, end_i, end_j, color = map(int, input().split())
    record += [[start_i, start_j, end_i, end_j, color]]
    if color == 1:
        another_color = 2
    elif color == 2:
        another_color = 1
    
    for j in range(start_j, end_j+1):
        for i in range(start_i, end_i+1):
            if paper[i][j] == another_color: # 해당 위치에 내가 칠할 색이 아닌 다른색이 칠해져 있다면
                paper[i][j] = 3
            else:
                paper[i][j] = color
for _ in range(10):
    print(paper[_])
print(check_purple_len(paper))