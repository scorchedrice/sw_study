def dfs(n,height):
    global mn
    if height >= B:
        if mn > height:
            mn = height
            return
    if n == N:
        return
    dfs(n+1, height + arr[n])
    dfs(n+1, height)

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    arr = list(map(int,input().split()))
    mn = 987654321
    dfs(0,0)
    print(f"#{tc} {mn-B}")