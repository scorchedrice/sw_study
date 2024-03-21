from pprint import pprint

# 해당 조건을 만족하려면 한 바퀴를 돌거나, 꼭지점부터 시작해서 끝 꼭지점으로 도착하면 된다.
# 즉, 꼬다리가 있으면 꼬다리에서 시작하면 무조건 결론을 도출한다.
    # 꼬다리는 해당 블럭을 기준으로 3방향에 아무것도 없으면 이를 시작점으로 볼 수 있다.
# 하지만, 꼬다리가 없다면? 이는 사이클을 도는 경우라고 볼 수 있다.
# 즉, 이 경우에는 꼭짓점, matrix를 받을 때 처음으로 마주하는 '#'을 시작점으로 보면 된다
'''
7 5 
..###
..#.#
###.#
....#
..#.#
..#.#
..###
이 경우에 (0,2)가 아닌 (2,0)이 나오도록 시작지점을 잡는 과정 필요
'''

def find_start(arr):
    tmp = []
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#':
                if tmp == []:
                    for dir in range(4):
                        mi = i + delta[dir][0]
                        mj = j + delta[dir][1]
                        if 0<=mi<H and 0<=mj<W:
                            if matrix[mi][mj] == '#':
                                if dir == 0: # 상
                                    tmp.append((i,j,'^'))
                                elif dir == 1: # 하
                                    tmp.append((i,j,'v'))
                                elif dir == 2: # 좌
                                    tmp.append((i,j,'<'))
                                else:
                                    tmp.append((i,j,'>'))
                        if tmp != []:
                            break
                                # 탐색을 하면서 만약 꼬다리를 찾지 못한다면 이 값을 리턴할 예정
                cnt = 0
                dir_tmp = []
                for dir in range(4):
                    mi = i + delta[dir][0]
                    mj = j + delta[dir][1]
                    if 0<=mi<H and 0<=mj<W:
                        if matrix[mi][mj] == '#':
                            cnt += 1
                            if dir_tmp == []:
                                # print(mi,mj,dir)
                                if dir == 0: # 상
                                    dir_tmp.append((i,j,'^'))
                                elif dir == 1: # 하
                                    dir_tmp.append((i,j,'v'))
                                elif dir == 2: # 좌
                                    dir_tmp.append((i,j,'<'))
                                else:
                                    dir_tmp.append((i,j,'>'))
                if cnt >= 2:
                    break
                if cnt == 1: # 꼬다리를 찾았으니 이 값을 리턴
                    return dir_tmp[0]
    return tmp[0]
            
delta = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
'''
상으로 이동 중 L:좌, R:우
하로 이동 중 L:우, R:좌
좌로 이동 중 L:하, R:상
우로 이동 중 L:상, R:하
'''
def change_dir(current_dir, target_dir):
    if current_dir == (-1,0): # 상으로 이동 중이라면
        if target_dir == (0,-1):
            return 'L'
        else:
            return 'R'
    elif current_dir == (1,0): # 하로 이동중이라면
        if target_dir == (0,1):
            return 'L'
        else:
            return 'R'
    elif current_dir == (0,-1): # 좌로 이동중이라면
        if target_dir == (1,0):
            return 'L'
        else:
            return 'R'
    elif current_dir == (0,1): # 우로 이동중이라면
        if target_dir == (-1,0):
            return 'L'
        else:
            return 'R'

def move_robot(si,sj):
    global order_str
    matrix[si][sj] = '.'
    ci, cj = si, sj
    if first_dir == '^':
        current_dir = 0
    elif first_dir == 'v':
        current_dir = 1
    elif first_dir == '<':
        current_dir = 2
    else:
        current_dir = 3
    # 이 경우 다시 돌아가는 경우는 고려하지 않으므로 스택은 필요없음.
    while True:
        for dir in range(4):
            mi2 = ci + 2*delta[dir][0]
            mj2 = cj + 2*delta[dir][1]
            mi1 = ci + delta[dir][0]
            mj1 = cj + delta[dir][1]
            if 0<=mi2<H and 0<=mj2<W:
                if matrix[mi1][mj1] == '#' and matrix[mi2][mj2] == '#':
                    matrix[mi1][mj1] = '.'
                    matrix[mi2][mj2] = '.'
                    ci = mi2
                    cj = mj2
                    if current_dir != dir:
                        order_str += change_dir(delta[current_dir], delta[dir])
                    current_dir = dir
                    order_str += 'A'
                    break
        else:
            # 반복문이 다 돌아도 방향을 못찾는다 == 더이상 갈 곳이 없다.
            # pprint(matrix)
            return


matrix = []
H, W = map(int,input().split())

for _ in range(H):
    matrix.append(list(input()))
# pprint(matrix)
start = find_start(matrix)
first_dir = start[2]
order_str = ''
move_robot(start[0],start[1])

print(start[0]+1,end = ' ')
print(start[1]+1)
print(first_dir)
print(order_str)