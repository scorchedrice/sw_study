A = 0
B = 99

def DFS():
    visited = [0] * (100) # 0번부터 99번까지의 방문기록 리스트
    # while문 종료 후 99번이 True라면 방문 가능하다고 취급함.
    visited[0] = True
    now = 0 # 0번에서 시작함.
    stack = [0] # 이동해온 경로를 기록하기 위함
    while True:
        
        for k in range(len(map_info[now])):
            if visited[map_info[now][k]] == 0:
                now = map_info[now][k]
                visited[now] = 1
                stack += [now]
                break
            
        else:
            if stack == []:
                return visited[99]
            else:
                now = stack.pop()

for tc in range(1,11):
    map_info = [[] for _ in range(100)] # 0번부터 99번까지 노드/간선 정보 기록 위함.
    testcase, route_num = map(int,input().split())
    route_info = list(map(int,input().split()))
    for k in range(route_num):
        map_info[route_info[2*k]] += [route_info[2*k+1]]
    print(f"#{testcase} {DFS()}")