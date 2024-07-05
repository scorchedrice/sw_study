from collections import deque

pivot = 1
result = []
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def index_check(ti, tj):
    if 0 <= ti < N and 0 <= tj < N and matrix[ti][tj] == '1':
        return True
    else:
        return False

def fix_number(i, j):
    global pivot
    global result
    numbering = 1
    nowI = i
    nowJ = j
    matrix[nowI][nowJ] = pivot
    queI = deque()
    queJ = deque()
    while True:
        # print(queI, queJ)
        for dir in range(4):
            targetI = nowI + di[dir]
            targetJ = nowJ + dj[dir]
            if index_check(targetI, targetJ) == True:
                queI.append(targetI)
                queJ.append(targetJ)
                matrix[targetI][targetJ] = pivot
                numbering += 1
        if queI == deque():
            pivot += 1
            result.append(numbering)
            return
        else:
            nowI = queI.popleft()
            nowJ = queJ.popleft()

def fix_matrix():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '1':
                fix_number(i, j)
    # print(matrix)

N = int(input())
# size

matrix = []
for size in range(N):
    layer = list(input())
    matrix += [layer]
fix_matrix()

total = len(result)
result = sorted(result)
print(total)
for _ in range(total):
    print(result[_])
