ground = '.'
wall_brick = '*'
wall_steel = '#'
water = '-'
tank_up = '^'
tank_down = 'v'
tank_right = '>'
tank_left = '<'
def find_tank():
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == '<':
                return i,j,'L'
            if matrix[i][j] == '>':
                return i,j,'R'
            if matrix[i][j] == 'v':
                return i,j,'D'
            if matrix[i][j] == '^':
                return i,j,'U'
def shoot(now_dir):
    global matrix
    start_i = now_i
    start_j = now_j
    shoot_dir = now_dir
    if shoot_dir == 'U':
        go = (-1,0)
    elif shoot_dir == 'D':
        go = (1,0)
    elif shoot_dir == 'L':
        go = (0,-1)
    elif shoot_dir == 'R':
        go = (0,1)
    while True:
        start_i += go[0]
        start_j += go[1]
        if 0<=start_i<= H-1 and 0<=start_j<=W-1:
            if matrix[start_i][start_j] == '*':
                matrix[start_i][start_j] = '.'
                break
            elif matrix[start_i][start_j] == wall_steel:
                break
        if start_i < 0 or start_i > H or start_j < 0 or start_j > W:
            break
def move_tank(action):
    global now_i
    global now_j
    global now_dir
    if action == 'U':
        move_i = now_i - 1
        now_dir = 'U'
        if 0<=move_i<=H-1 and matrix[move_i][now_j] == '.':
            matrix[move_i][now_j] = '^'
            matrix[now_i][now_j] = ground
            now_i = move_i
        else:
            matrix[now_i][now_j] = '^'
    elif action == 'D':
        move_i = now_i + 1
        now_dir = 'D'
        if 0<=move_i<=H-1 and matrix[move_i][now_j] == ground:
            matrix[move_i][now_j] = 'v'
            matrix[now_i][now_j] = ground
            now_i = move_i
        else:
            matrix[now_i][now_j] = 'v'
    elif action == 'L':
        move_j = now_j - 1
        now_dir = 'L'
        if 0<=move_j<=W-1 and matrix[now_i][move_j] == ground:
            matrix[now_i][move_j] = '<'
            matrix[now_i][now_j] = ground
            now_j = move_j
        else:
            matrix[now_i][now_j] = '<'
    elif action == 'R':
        move_j = now_j + 1
        now_dir = 'R'
        if 0<=move_j<=W-1 and matrix[now_i][move_j] == '.':
            matrix[now_i][move_j] = '>'
            matrix[now_i][now_j] = '.'
            now_j = move_j
        else:
            matrix[now_i][now_j] = '>'
    elif action == 'S':
        shoot(now_dir)

T = int(input())
for tc in range(1,T+1):
    H, W = map(int,input().split())
    # H는 높이, W는 너비
    matrix = []
    for i in range(H):
        matrix.append(list(input()))
    actions = int(input())
    action_lst = list(input())
    now_i, now_j, now_dir = find_tank()
    for action in range(actions):
        move_tank(action_lst[action])
        
    print(f"#{tc}", end = ' ')
    for _ in range(H):
        print(''.join(matrix[_]))
