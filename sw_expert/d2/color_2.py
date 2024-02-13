# T = int(input())
# for tc in range(1,T+1):
def dfs_purple(i,j):
    di = [0,1,0,-1] # 북 동 남 서
    dj = [-1,0,1,0]
    current_i = i
    current_j = j
    stack_i = []
    stack_j = []
    x_list = [1]
    y_list = [1]
    while True:
        for dir in range(4):
            if 0<=current_i+di[dir]<=N-1 and 0<=current_j+dj[dir]<=N-1 and paper[current_i + di[dir]][current_j + dj[dir]] == 3:
                # index를 만족하면서 이동할 경로가 보라색이라면
                stack_i += [current_i] # 방문 위치를 push
                stack_j += [current_j]
                paper[current_i][current_j] = 4 # 방문한 위치에 방문 흔적을 남기고
                current_i += di[dir] # 해당 좌표로 이동하고
                x_list += [x_list[-1] + di[dir]] # 변화량을 작성한다.
                current_j += dj[dir]
                y_list += [y_list[-1] + dj[dir]]
                break
        else: # 만약 4가지 방향에서 갈 길을 찾지 못하고
            if stack_i == []: # stack이 비어있다면
                paper[current_i][current_j] = 4
                break # while loop를 종료하고
            else: # 그 외의 경우에는 , stack의 마지막을 현 위치로 지정한다.
                current_i = stack_i.pop()
                current_j = stack_j.pop()
    return x_list + y_list

def check_purple_len(paper):
    result = []
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                result += [dfs_purple(i,j)] # 탐색을 진행하고 탐색 결과 보라색의 길이를 가져온다.
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