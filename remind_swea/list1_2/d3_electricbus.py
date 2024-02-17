'''
0번에서 출발하는 버스
종점인 N번인 정류장까지 가려고 한다.
한번 충전으로는 K개의 정류장을 이동할 수 있다.
충전기가 설치된 정류장은 M개로, 정류장 번호가 주어진다.
최소한 몇번의 충전을 해야 종점에 도착할 수 있는가
충전기가 잘못 설치되어 도착할 수 없는 경우, 0을 출력한다.
'''
'''
DFS느낌으로 할 수 있을것만 같아
'''
def move_check():
    current = 0
    bus_move = 0
    stack = []
    while True:
        # 최대한 가본 후 충전소의 위치를 기록한다.
        for move in range(K):
            current += 1
            if current == N:
                # 만약 종점에 도착하면 종료한다.
                return bus_move
            elif real_map[current] == 'Charger':
                stack += [current]
        print(stack)
        # 이후 충전소의 위치가 확인되지 않는다면, 반복문을 종료한다.
        if stack == []:
            return 0
        else:
            # 충전기가 존재하는 곳까지 갈 수 있다면
            current = stack[-1]
            stack = []
            bus_move += 1
    return

#T = int(input())
K, N, M = map(int,input().split())
# K는 배터리 용량, N은 종점번호, M은 충전기가 설치된 정류장 수를 의미한다.

# 아래의 코드를 통해 충전기의 위치를 표시한다.
M_list = list(map(int,input().split()))
real_map = [0] * (N+1)
for k in M_list:
    real_map[k] = 'Charger'
print(real_map)
print(move_check())
