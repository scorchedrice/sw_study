# 직사각형
'''
직사각형 정보 두개를 주고
이 직사각형들이 겹치는 부분이
a. 직사각형
b. 선분 (접하냐)
c. 점 (한 점에서 만나냐)
d. 공통부분이 없음
판별
'''
'''
주는 값은 좌측 하단 (x,y) 우측 상단 (x,y)

주어지는 값을 a,b,c,d라고 한다면
(a,d)(c,d)
(a,b)(c,b)
'''
def det_line_or_rec(matrix):
    for x in range(1000):
        for y in range(1000):
            if matrix[x][y] == 2:
                # check_left_index = [x-1,y]
                # check_right_index = [x+1,y]
                # check_up_index = [x,y+1]
                # check_down_index = [x,y-1]
                if 0<=x-1 and y+1<=1000: # 좌 상 비교
                    if matrix[x-1][y] == 2 and matrix[x][y+1] == 2:
                        return 1
                if 0<=x-1 and 0<=y-1: # 좌 하 비교
                    if matrix[x-1][y] == 2 and matrix[x][y-1] == 2:
                        return 1
                if x+1<=1000 and y+1<=1000: # 우 상 비교
                    if matrix[x+1][y] == 2 and matrix[x][y+1] == 2:
                        return 1
                if x+1<=1000 and 0<=y-1: # 우 하 비교
                    if matrix[x+1][y] == 2 and matrix[x][y-1] == 2:
                        return 1
                return 2
    
T = int(input())
for tc in range(1,T+1):
    matrix = [[0 for _ in range(1001)] for _ in range(1001)]

    A,B,C,D= map(int,input().split())
    a,b,c,d= map(int,input().split())
    check = 0
    for x1 in range(A,C+1):
        for y1 in range(B,D+1):
            matrix[x1][y1] += 1
    for x2 in range(a,c+1):
        for y2 in range(b,d+1):
            matrix[x2][y2] += 1
            if matrix[x2][y2] == 2:
                check += 1
    if check == 0:
        print(f"#{tc} 4")
    elif check == 1:
        print(f"#{tc} 3")
    elif check >= 2:
        print(f"#{tc} {det_line_or_rec(matrix)}")
