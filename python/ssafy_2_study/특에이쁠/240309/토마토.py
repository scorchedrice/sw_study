'''
100*100*100 의 스케일이길래 좌표를 사용하려 했었으나, 생각보다 큰 규모가 아니므로 정상적으로 bfs를 사용해도 괜찮다.
3차원일지라도 2차원 배열로 이를 표현할 수 있으며, matrix를 형성하는 과정과 탐색하는 과정의 순서가 약간 다를뿐이다.
더불어 문제에서 주어진, "모두 익은 토마토로 전환 불가한 경우"의 케이스에 걸리는 것을 추가 조건으로 달아야하며
익은 토마토만 존재하는 경우도 미리 확인해야한다.

따라서 극단적인 테스트케이스를 한번 입력해 볼 이유가 있는 것 같다.
스케일이 작거나, 크거나 혹은 한가지로만 이뤄진 상황이라거나
'''
from collections import deque

def bfs():
    dif = [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)] # 주변 토마토 확인 목적
    mx = -1
    now = Q.popleft()
    while True:
        for dir in range(6):
            dx = now[0] + dif[dir][0]
            dy = now[1] + dif[dir][1]
            dz = now[2] + dif[dir][2]
            if 0<=dx<=length-1 and 0<=dy<=width-1 and 0<=dz<=height-1 and matrix[dz][dy][dx] == 0:
                Q.append((dx,dy,dz))
                matrix[dz][dy][dx] = matrix[now[2]][now[1]][now[0]] + 1
                mx = matrix[now[2]][now[1]][now[0]] + 1
        if Q == deque():
            for x in range(length):
                for y in range(width):
                    for z in range(height):
                        if matrix[z][y][x] == 0:
                            return -1
            return mx - 1
        else:
            now = Q.popleft()

length, width, height = map(int,input().split())
matrix = [[] * width for _ in range(height)]

for z in range(height):
    for y in range(width):
        matrix[z].append(list(map(int,input().split())))

Q = deque()
unripe = 0
ripe = 0
for x in range(length):
    for y in range(width):
        for z in range(height):
            if matrix[z][y][x] == 1:
                Q.append((x,y,z))
                ripe += 1
            elif matrix[z][y][x] == 0:
                unripe += 1

if unripe == 0:
    print('0')
elif ripe == 0:
    print('-1')
else:
    print(bfs())