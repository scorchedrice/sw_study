def dfs(route_data):
    start = 0
    visited = [False for _ in range(100)]
    visited[start] = True
    stack = []
    while True:
        for l in route_data[start]: # 시작 지점에서 갈 수 있는 후보들을 조사하겠다.
            if visited[l] == False: # 만약 갈 수 있는 지점이 확인된다면
                stack += [start] # stack에 추가하고
                start = l # 해당 지점으로 이동한다.
                visited[l] = True # 이후 방문 기록을 남긴다.
                break

        else: # for loop를 다 돌렸는데도 갈 수 있는 경로를 찾지 못한경우
            if stack == []:
                break # 이 때 stack이 비어있는 경우엔 while을 중단한다.
            else: # 그렇지 않고 남아있다면
                start = stack.pop() # 그 전 경로로 이동한다.
    # dfs탐색 이후 결론 도출
    for k in end_list:
        if visited[k] == True: # B와 연결된 다리가 있는 곳에 도달한 기록이 확인된다면
            return 1
    else: # B와 연결된 다리가 있는 곳에 도달한 기록을 찾지 못한 경우
        return 0
                
T = 10
for test_case in range(1,T+1):
    tc, N = map(int, input().split())

    map_data = list(map(int, input().split())) # map 정보 입력

    route_data = [[] for _ in range(100)]
    for i in range(len(map_data)): # route data 생성
        if i%2 == 0:
            route_data[map_data[i]] += [map_data[i+1]]

    end_list = []
    for i in range(len(map_data)): # end 찾기
            if map_data[i] == 99:
                end_list += [map_data[i-1]]

    print(f"#{tc} {dfs(route_data)}")