# 상하좌우
# start = (1,1), L = 좌1, R = 우1, U = 상1, D = 하1
# 문제 풀이 전 가정 : 리스트를 읽고 좌표를 이동한다. 좌표에 따라 일정 명령은 무시하는 조건을 추가한다.
'''
# 어떤 좌표일때 어떤 명령을 무시할까
if (1,*) ... U
if (*,1) ... L
if (N,*) ... D
if (*,N) ... R
'''



N = int(input()) # 격자 사이즈
move = list(map(str, input().split())) # 이동 경로
max_distance = len(move) # 최대한 움질일 수 있는 칸, 최대를 가정하고 반복문 사용
position = [1,1] # 초기 위치 (1,1)로 가정
for dir in move: # 위에서 정한 제한 조건을 적용한 loop
    if dir == 'R':
        if position[1] == N:
            continue
        else:
            position[1] += 1
    if dir == 'L':
        if position[1] == 1:
            continue
        else:
            position[1] -= 1
    
    if dir == 'D':
        if position[0] == N:
            continue
        else:
            position[0] += 1
    if dir == 'U':
        if position[0] == 1:
            continue
        else:
            position[0] -= 1

print(position[0], end = ' ') # 공백으로 출력하기 위해
print(position[1], end = ' ')
