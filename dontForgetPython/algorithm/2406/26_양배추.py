from collections import deque
# 덩어리 구하기 문제

di = [0,0,-1,1]
dj = [-1,1,0,0]

def bfs(i,j):
    global bug
    # 벌레의 수 덩어리마다 하나씩 추가
    queI = deque([i])
    queJ = deque([j])
    nowI = i
    nowJ = j
    matrix[i][j] = 0
    while True:
        for dir in range(4):
            nextI = nowI + di[dir]
            nextJ = nowJ + dj[dir]
            if 0<=nextI<row and 0<=nextJ<col:
                # index 조건 만족
                if matrix[nextI][nextJ] == 1:
                    queI.append(nextI)
                    queJ.append(nextJ)
                    matrix[nextI][nextJ] = 0
        if queI == deque() and queJ == deque():
            bug += 1
            break
        else:
            nowI = queI.popleft()
            nowJ = queJ.popleft()

T = int(input())
for tc in range(1,T+1):
    bug = 0
    row, col, plant = map(int,input().split())
    matrix = [[0]*col for _ in range(row)]
    # 여기선 가로세로 사실 안중요하니, 일관성있게 풀이 ㄱㄱ
    for seed in range(plant):
        r, c = map(int,input().split())
        matrix[r][c] = 1

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                bfs(i,j)
    print(bug)
