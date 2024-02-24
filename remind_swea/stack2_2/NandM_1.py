N, M = map(int,input().split())

def dfs(n,lst):
    if n == M:
        ans.append(lst)
        return
    for _ in range(1,N+1):
        if visited[_] == 0:
            visited[_] = 1
            dfs(n+1,lst+[_])
            visited[_] = 0

visited = [0]  * (N+1)
ans = []
dfs(0,[])
for k in range(len(ans)):
    print(*ans[k])