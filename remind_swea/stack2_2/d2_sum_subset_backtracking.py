def dfs(n, lst):
    if n > list_A_len:
        if sum(lst) == K and len(lst) == N:
            ans.append(lst)
        return
    dfs(n+1,lst+[n])
    dfs(n+1,lst)

T=int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    # N은 원소의 수, K는 집합의 합
    list_A_len = 12
    ans = []
    dfs(1,[])
    print(f"#{tc} {len(ans)}")