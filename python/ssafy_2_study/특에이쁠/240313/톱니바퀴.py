# 164ms
from collections import deque
from copy import deepcopy
def bfs(target, dir):
    dir_tmp = deepcopy(dir) # 임의로 저장 후 좌측 탐색 시 이를 다시 불러옴
    v = [0] * 4
    v[target] = dir
    # idx == 2 : right, idx == 6 : left
    pivot_p = gears[target][2]
    pivot_l = gears[target][6]
    now = target
    # 우측으로 확인하는 작업 진행
    while True:
        mv = now + 1
        if 0<=mv<=3 and v[mv] == 0:
            right_pivot = gears[mv][6]
            if right_pivot == pivot_p:
                break
            else:
                now = mv
                if dir == 1:
                    v[now] = -1
                    dir = -1
                    pivot_p = gears[now][2]
                elif dir == -1:
                    v[now] = 1
                    dir = 1
                    pivot_p = gears[now][2]
        else:
            break
    
    now = target
    dir = deepcopy(dir_tmp)
    # 좌측으로 확인하는 작업 진행
    while True:
        mv = now -1
        if 0<=mv<=3 and v[mv] == 0:
            left_pivot = gears[mv][2]
            if left_pivot == pivot_l:
                break
            else:
                now = mv
                if dir == 1:
                    v[now]  = -1
                    dir = -1
                    pivot_l = gears[now][6]
                elif dir == -1:
                    v[now] = 1
                    dir = 1
                    pivot_l = gears[now][6]
        else:
            break
    return v

# -1이면 반시계, 1이면 시계
# 시계방향 회전, 반시계방향 회전 함수를 위 탐색 결과에 따라 진행.
def clock(rotate_info):
    global gears
    for i in range(4):
        if rotate_info[i] == 1:
            gears[i].appendleft(gears[i].pop())
    return

def rev_clock(rotate_info):
    global gears
    for i in range(4):
        if rotate_info[i] == -1:
            gears[i].append(gears[i].popleft())
    return

gear1 = deque(list(input()))
gear2 = deque(list(input()))
gear3 = deque(list(input()))
gear4 = deque(list(input()))
gears = [gear1, gear2, gear3, gear4]

N = int(input())
for _ in range(N):
    gear, rot = map(int,input().split())
    rotate_info = bfs(gear-1, rot)
    clock(rotate_info)
    rev_clock(rotate_info)

result = 0
for k in range(4):
    check = gears[k][0]
    if check == '1':
        result += (2**k)
print(result)