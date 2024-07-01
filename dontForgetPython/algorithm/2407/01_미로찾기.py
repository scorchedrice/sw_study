from collections import deque

di = [0,0,-1,1]
dj = [1,-1,0,0]

def bfs():
    queI = deque([])
    queJ = deque([])
    nowI = 0
    nowJ = 0
    matrix[0][0] = 1
    while True:
        for dir in range(4):
            nextI = nowI + di[dir]
            nextJ = nowJ + dj[dir]
            if 0<=nextI<n and 0<= nextJ < m and matrix[nextI][nextJ] == '1':
                matrix[nextI][nextJ] = matrix[nowI][nowJ] + 1
                # 현 위치의 + 1 값을 다음 좌표에 할당
                queI.append(nextI)
                queJ.append(nextJ)
                # que에 이동 가능 후보를 append
        if queI == deque([]):
            print(matrix[n-1][m-1])
            break
        else:
            nowI = queI.popleft()
            nowJ = queJ.popleft()

n, m = map(int,input().split())
matrix = []
for _ in range(n):
    input_data = input()
    input_layer = []
    for __ in range(m):
        input_layer += input_data[__]
    matrix += [input_layer]

bfs()
