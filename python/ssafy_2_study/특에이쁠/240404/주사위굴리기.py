# 주사위 굴리기 148ms
'''
맨 처음 0으로 칠해져 있는 주사위
지도에 있는 숫자가 주사위에 칠해짐
단, 지도의 숫자가 0이면 주사위의 숫자가 칸에 칠해짐
'''
'''
문제풀이 방향 
    - 종과 횡 구분 / 공간도형 활용
    - 종이동시 동쪽서쪽 주사위의 횡이동 절대위치는 변하지 않는다.
    - 마찬가지로 횡이동시 북쪽남쪽 주사위의 종이동 절대위치는 변하지 않는다.
* 종이동(34)와 횡이동(12)의 순서를 따로 본다.
    - 횡이동 idx의 경우 deque([top, 동, bot, 서])
    - 종이동 idx의 경우 deque([top, 북, bot, 남])
    - 숫자 값을 적는 것이 아닌, 주사위의 주소? 를 deque로 하였고 주사위에 적히는 숫자 정보는 dict. 활용
* 방향에 따라 rotate 하는 함수를 정의한다.
    - idx를 벗어나는 명령을 내리는 경우 이를 무시해야 하므로 ignore 을 global로 정의
        - True 인 경우 print 하지 않고 반복문 진행
    - idx내인 경우 해당하는 방향으로 rotate()
* top과 bot을 계속 수정해가면서, 횡이동 이후 종이동, 종이동 이후 횡이동하는 경우 idx를 수정하는 과정을 거친다.
    - 함수로 정의해서 이 과정을 진행했음.
'''
from collections import deque
dice_idx_12 = deque([1,3,6,4])
# dir == 1,2인경우
# 동쪽으로 이동 : 1364 4136 6413 ...
dice_idx_34 = deque([1,2,6,5])
# dir == 3,4인경우
# 북쪽으로 이동 : 1265 5126 6512 ...

dice_num = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
def rotate1(si,sj):
    global top
    global bot
    global ignore
    ci = si
    cj = sj
    mj = cj + 1
    if 0<=mj<M: # 굴리는 범위가 인덱스를 만족한다면
        cj = mj
        # ci,cj가 이동할 좌표
        # 동쪽으로 갔으니 rotate(1)
        dice_idx_12.rotate(1)
        top = dice_idx_12[0]
        bot = dice_idx_12[2]
        if matrix[ci][cj] != 0:
            dice_num[dice_idx_12[2]] = matrix[ci][cj]
            matrix[ci][cj] = 0
        else:
            matrix[ci][cj] = dice_num[dice_idx_12[2]]
        return (ci,cj)
    else:
        ignore = True
        return (si,sj)

def rotate2(si,sj):
    global top
    global bot
    global ignore
    ci = si
    cj = sj
    mj = cj - 1
    if 0<=mj<M: # 굴리는 범위가 인덱스를 만족한다면
        cj = mj
        dice_idx_12.rotate(-1)
        top = dice_idx_12[0]
        bot = dice_idx_12[2]
        if matrix[ci][cj] != 0:
            dice_num[dice_idx_12[2]] = matrix[ci][cj]
            matrix[ci][cj] = 0
        else:
            matrix[ci][cj] = dice_num[dice_idx_12[2]]
        return (ci,cj)
    else:
        ignore = True
        return (si,sj)

def rotate3(si,sj):
    global top
    global bot
    global ignore
    ci = si
    cj = sj
    mi = ci - 1
    if 0<=mi<N:
        ci = mi
        dice_idx_34.rotate(1)
        top = dice_idx_34[0]
        bot = dice_idx_34[2]
        if matrix[ci][cj] != 0:
            dice_num[dice_idx_34[2]] = matrix[ci][cj]
            matrix[ci][cj] = 0
        else:
            matrix[ci][cj] = dice_num[dice_idx_34[2]]
        return (ci,cj)
    else:
        ignore = True
        return (si,sj)

def rotate4(si,sj):
    global top
    global bot
    global ignore
    ci = si
    cj = sj
    mi = ci + 1
    if 0<=mi<N:
        ci = mi
        dice_idx_34.rotate(-1)
        top = dice_idx_34[0]
        bot = dice_idx_34[2]
        if matrix[ci][cj] != 0:
            dice_num[dice_idx_34[2]] = matrix[ci][cj]
            matrix[ci][cj] = 0
        else:
            matrix[ci][cj] = dice_num[dice_idx_34[2]]
        return (ci,cj)
    else:
        ignore = True
        return (si,sj)

def fixed_idx(ex_dir, dir):
    if ex_dir == 0:
        return
    elif ex_dir == 1 or ex_dir == 2:
        if dir == 3 or dir == 4: # 종 횡 이동 방향성이 바뀐 경우
            # 횡이동 => 종이동
            dice_idx_34[0] = top
            dice_idx_34[2] = bot
    elif ex_dir == 3 or ex_dir == 4:
        if dir == 1 or dir == 2:
            # 종이동 => 횡이동
            dice_idx_12[0] = top
            dice_idx_12[2] = bot
    return

N,M,ci,cj,K = map(int,input().split())
matrix = []
for k in range(N):
    matrix.append(list(map(int,input().split())))
order_lst = list(map(int,input().split()))
top = 1
bot = 6
ex_dir = 0
ignore = False
for l in range(K):
    dir = order_lst[l]
    # print(dice_idx_12)
    # print(dice_idx_34)
    # print('--------')
    fixed_idx(ex_dir,dir)
    # print(dice_idx_12)
    # print(dice_idx_34)
    ex_dir = dir
    if dir == 1:
        ci,cj = rotate1(ci,cj)
    elif dir == 2:
        ci,cj = rotate2(ci,cj)
    elif dir == 3:
        ci,cj = rotate3(ci,cj)
    else:
        ci,cj = rotate4(ci,cj)
    # print(top)
    # print(dice_num)
    # print('###############')
    if ignore == False:
        print(dice_num[top])
    ignore = False
    # print('##############')