from collections import deque

T = int(input())
for tc in range(1,T+1):
    island, bridge = map(int, input().split())
    island_info = [0 for _ in range(island+1)]
    # index가 island_number

    map_info = []
    for _ in range(bridge):
        map_info += [list(map(int, input().split()))]
    real_map = [[] for _ in range(island+1)]
    for k in range(bridge):
        real_map[map_info[k][0]] += [map_info[k][1]]
        real_map[map_info[k][1]] += [map_info[k][0]]
    start, end = map(int,input().split())

    current = start
    Q = deque([])
    island_info[current] = 1
    # 나중에 1 빼서 결론 도출
    while True:
        for i in range(len(real_map[current])):
            if island_info[real_map[current][i]] == 0:
                deque.append(Q, real_map[current][i])
                island_info[real_map[current][i]] = island_info[current] + 1
        else:
            if Q == deque([]):
                break
            else:
                current = deque.popleft(Q)

    if island_info[end] != 0:
        print(f"#{tc} {island_info[end]-1}")
    else:
        print(f"#{tc} 0")
