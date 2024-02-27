# 2669 - 직사각형 네개의 합집합 면적 구하기
matrix = [[0 for _ in range(101)] for _ in range(101)]

# 주는 꼭짓점 : 왼쪽 하단, 오른쪽 상단
# 왼쪽 아래 x좌표 왼쪽 아래 y좌표 우측 상단 x좌표 우측 상단 y좌표
for _ in range(4):
    L_x, L_y, R_x, R_y = map(int,input().split())
    for x in range(L_x, R_x):
        for y in range(L_y, R_y):
            matrix[x][y] = 1

cnt = 0
for x in range(1,101):
    for y in range(1,101):
        if matrix[x][y] == 1:
            cnt += 1
print(cnt)