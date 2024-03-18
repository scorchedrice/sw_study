# 컨베이어 벨트 위 로봇
'''
1번칸 : 올리는 위치
N번칸 : 내리는 위치
로봇은 올리는 위치에서만 올릴 수 있고 내리는 위치에 도달하면 즉시 내린다.
로봇이 칸을 이동하거나 해당 위치에 올라간다면 해당 칸의 내구도는 1 감소한다.
'''
'''
1. 벨트가 각 칸 위에 있는 로봇과 함께 한칸 회전한다.
2. "가장 먼저 벨트에 올라간 로봇부터", 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
    - 로봇의 이동에 순서 존재
    - 로봇이 이동하기 위해선 이동하려는 칸에 로봇이 없어야 하고, 그 칸의 내구도가 1 이상 있어야
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
'''
from collections import deque

def push_robot():
    global belt_info
    # 첫번째 컨베이어 벨트 칸의 내구도가 충분하냐
    if belt_info[0][1] >= 1:
        belt_info[0][2] += 1 # 1은 로봇이 있다는 이야기
        belt_info[0][1] -= 1
        

def pop_robot():
    # N번 (N-1 index) 컨베이어 벨트 칸의 로봇이 있냐
    global belt_info
    if belt_info[N-1][2] == 1:
        belt_info[N-1][2] -= 1

def move_robot():
    global belt_info
    # 벨트 이동 후 로봇 이동하는 과정 진행
    for i in range(N-2,-1,-1):
        if belt_info[i][2] == 1 and belt_info[i+1][1] >= 1 and belt_info[i+1][2] != 1:
            # 로봇이 있고 다음칸의 내구도가 충분하면서 로봇이 존재하지 않는 경우
            belt_info[i][2] -= 1
            belt_info[i+1][2] += 1
            belt_info[i+1][1] -= 1

def run_belt():
    global belt_info
    belt_info.appendleft(belt_info.pop())
    
def check_zero():
    result = 0
    for i in range(2*N):
        if belt_info[i][1] <= 0:
            result += 1
    return result

N, K = map(int,input().split())
# N은 물건을 내려 놓을 좌표, K 는 정지 조건 (내구도 0인 것 K개)

robot_in = 0
robot_out = N-1 # idx

belt_info = deque()
belt_life = list(map(int,input().split()))
for k in range(2*N):
    life = belt_life[k] # 내구도
    belt_info.append([k,life,0])

cnt = 0
while True:
    run_belt()
    cnt += 1

    pop_robot()
    
    move_robot()
    cnt += 1

    pop_robot()
    
    push_robot()
    cnt += 1
    
    pivot = check_zero()
    if pivot >= K:
        break
print(int(cnt/3))