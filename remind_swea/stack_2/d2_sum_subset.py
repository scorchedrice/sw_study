def dfs(n,lst):
    if n>12:
        if sum(lst) == K and len(lst) == N:
            ans.append(lst)
        return
    dfs(n+1, lst+[n])
    dfs(n+1, lst)
    
def subset_bit(arr):
    result = []
    for i in range(1<<12):
        memory = []
        for j in range(12):
            if i & (1<<j):
                memory += [arr[j]]
        if len(memory) == N and sum(memory) == K:
            result += [memory]
    return len(result)

T=int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    # N은 원소의 수, K는 원소의 합
    #ans = []
    #dfs(1,[])
    #print(f"#{tc} {len(ans)}")

    print(f"#{tc} {subset_bit(list(range(1,13)))}")
# 비트연산자를 활용한 함수를 이용한 경우

