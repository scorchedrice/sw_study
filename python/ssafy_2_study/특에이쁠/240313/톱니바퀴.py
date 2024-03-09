'''
톱니바퀴 4개 존재 (1번 ~ 4번)
톱니바퀴를 K번 회전 시키려 한다. (회전 시 시계 혹은 반시계회전)

A를 회전시키려 하는 상황 : 붙어있는 B의 극이 다르다면 A의 반대 방향으로 B는 회전한다.
'''
'''
톱니바퀴는 4개고, 홈의 개수는 정해져 있으므로 회전 시 양 극을 확인하기 쉬운 형태로 받아 리스트를 구성하자.
이 정보들을 기반으로 시계, 반시계 회전 결과를 반영하는 함수를 정의한다.
더불어, 하나의 톱니가 회전한 경우 주변 톱니가 회전하는 것을 결정하는 함수 또한 정의한다.
'''
'''
N극은 0, S극은 1로 주어진다. 12시를 기준으로 시계방향으로 주어진다.
1 0 1 0 1 1 1 1 ... 이와 같은 경우라면 3번 right, 7번 left
회전을 리스트 값을 pop, popleft하며 진행하므로 deque 활용
'''
from collections import deque
gear1 = deque(list(input()))
gear2 = deque(list(input()))
gear3 = deque(list(input()))
gear4 = deque(list(input()))

def check_rotate(target, dir):
    t_dir = [1,-1,1,-1,1,-1] # 회전시키는 기어 방향
    near_dir = [-1,1,-1,1,-1,1] # 인접한 기어 방향 (반대극인경우)
    
    if dir == 1:
        idx = 0
    elif dir == -1:
        idx = 1
    
    rotate_dir = []
    gear_info = [(gear1[7],gear1[3]),(gear2[7],gear2[3]),(gear3[7],gear3[3]),(gear4[7],gear4[3])]
    if target == 1:
        rotate_dir.append(t_dir[idx])
        if gear_info[0][1] != gear_info[1][0]: # 2
            rotate_dir.append(near_dir[idx])
            idx += 1
            if gear_info[1][1] != gear_info[2][0]: # 3
                rotate_dir.append(near_dir[idx])
                idx += 1
                if gear_info[2][1] != gear_info[3][0]: # 4
                    rotate_dir.append(near_dir[idx])
                    idx += 1
    while len(rotate_dir) != 4:
        rotate_dir.append(0)
    return rotate_dir

N = int(input())
for _ in range(N):
    target, dir = map(int,input().split())
    print(check_rotate(target, dir))
    



