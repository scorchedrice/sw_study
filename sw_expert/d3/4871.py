
T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())

    graph_info = []
    for i in range(E):
        graph_info += list(map(int, input().split()))

    graph_map = [[] for _ in range(V+1)]

    for j in range(0,2*E,2):
        graph_map[graph_info[j]] += [graph_info[j+1]]
        graph_map[graph_info[j+1]] += [graph_info[j]]

    print(graph_map)

    start_box, end_box = map(int, input().split())

    def dfs(start_box, end_box, V): #시작과 끝, 방문가능한 총 정점의 수
        visited = [0]*(V+1)
        stack = []
        visited[start_box] = 1 # 시작지점 방문, 방문 표시
        while True: # 탐색 시작
            # 현재 방문한 정점에 인접하고 방문안한 정점이 있으면
            for w in graph_map[start_box]:
                if visited[w] == 0: #해당 좌표가 이동 가능하다면
                    stack += [w] # push
                    start_box = w # 그 위치로 이동했다는 의미1
                    visited[start_box] = 1 # 그 위치로 이동했다는 의미2
                    break
                else: # start에 (옮긴 자리에) 인접 정점이 없다면
                    if stack != []: # 스택이 비어있지 않다면
                        start_box = stack.pop()
                    else: # 스택이 비어있는 경우 (현 위치 start)
                        break
            if visited[end_box] == 1:
                return 1
        
    print(f"#{tc} {dfs(start_box, end_box, V)}")



