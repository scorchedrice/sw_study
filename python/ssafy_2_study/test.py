# 주사위 굴리기
'''
맨 처음 0으로 칠해져 있는 주사위
지도에 있는 숫자가 주사위에 칠해짐
단, 지도의 숫자가 0이면 주사위의 숫자가 칸에 칠해짐
'''
from collections import deque
dice_idx_row = deque([1,3,6,4])
# 동쪽으로 이동 : 1364 4136 6413 ...
dice_idx_col = deque([1,2,6,5])
# 북쪽으로 이동 : 1265 5126 6512 ...
dice_num = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

def rotate_row(dir):
    global top
    global x
    global y
    if dir == 1:
        if 0<=x+1<N:
            x += 1
        else:
            return False
        dice_idx_row.rotate(1)
        top = dice_idx_row[0]
        bot = dice_idx_row[2]
        if bot == 0:
            dice_idx_row[2] = matrix[x][y]
            
        elif matrix[x][y] == 0:
            matrix[x][y] = dice_idx_row[2]
    elif dir == 2:
        if 0<=x-1<N:
            x += 1
        else:
            return False
        dice_idx_row.rotate(-1)
        top = dice_idx_row[0]
        bot = dice_idx_row[2]
        if bot == 0:
            dice_idx_row[2] = matrix[x][y]
        elif matrix[x][y] == 0:
            matrix[x][y] = dice_idx_row[2]




def rotate_col():
    pass

# N, M, x, y, K = map(int,input().split())
# N, M : size_map, x, y : 주사위를 놓은 곳 좌표, K 명령 수행 횟수
print(dice_idx_row)
dice_idx_row.rotate(1)
print(dice_idx_row)