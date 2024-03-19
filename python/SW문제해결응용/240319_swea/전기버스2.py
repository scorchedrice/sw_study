def dfs(n,btr,cnt):
    global mn
    btr = btr -1
    if btr < 0 or cnt >= mn:
        return
    if n == N-1:
        if mn > cnt:
            mn = cnt
        return
    dfs(n+1,arr[n],cnt+1)
    dfs(n+1,btr,cnt)

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr.pop(0)
    mn = 987654321
    dfs(1,arr[0],0)
    print(f"#{tc} {mn}")