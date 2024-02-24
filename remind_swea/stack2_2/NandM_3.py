def dfs(n,lst):
    if len(lst) == M:
        print(*lst)
        return
    if n>N:
        return
    for k in range(1,N+1):
        dfs(n+1, lst + [k])

N, M = map(int,input().split())
ans = []
dfs(0,[])