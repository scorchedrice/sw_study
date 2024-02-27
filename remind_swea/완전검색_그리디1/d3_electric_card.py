def dfs(n,lst):
    global min_value
    if n == need_to_search_num:
        result = battery[0][lst[0]-1]
        for k in range(need_to_search_num-1):
            result += battery[lst[k]-1][lst[k+1]-1]
        result += battery[lst[need_to_search_num-1]-1][0]
        if min_value > result:
            min_value = result
        return
    for i in range(need_to_search_num):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, lst+[need_to_search[i]])
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    battery = []
    for _ in range(N):
        battery += [list(map(int,input().split()))]

    need_to_search = list(range(2,N+1))
    need_to_search_num = N-1
    visited = [0] * need_to_search_num
    min_value = 987654321
    dfs(0,[])
    print(f"#{tc} {min_value}")