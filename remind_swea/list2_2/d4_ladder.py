def find_start():
    exit_i = 99
    exit_j = exit
    di = [-1,0,0] # 상 좌 우
    dj = [0,-1,1]

    current_i = exit_i
    current_j = exit_j
    while True:
        for dir in range(1,3): # 좌우를 우선 살핀다.
            move_j = current_j + dj[dir]
            if 0<=move_j<=99 and ladder[current_i][move_j] == 1:
                # 좌우에 갈 수 있는 곳이 있다면
                ladder[current_i][current_j] = 0
                current_j = move_j
                break
        else:
            ladder[current_i][current_j] = 1
            current_i -= 1
            if current_i == 0:
                return current_j



for tc in range(1,11):
    testcase = int(input())
    ladder = []
    for k in range(100):
        ladder += [list(map(int,input().split()))]

    exit = 0
    for l in range(100):
        if ladder[99][l] == 2:
            exit += l
            break
    print(f"#{tc} {find_start()}")