def dfs(n,total):
    global cnt
    if total == K:
        cnt += 1
        return
    if total > K:
        return
    if n > N-1:
        return
    
    dfs(n+1,total + lst[n])
    dfs(n+1,total)


T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    lst = list(map(int,input().split()))
    cnt = 0
    dfs(0,0)
    print(cnt)