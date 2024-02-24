def subset_bit(arr,n):
    N = len(arr)
    result = []
    for i in range(1<<N):
        memory = []
        for j in range(N):
            if i & (1<<j):
                memory += [arr[j]]
        if len(memory) == n and sum(memory) == K:
            result += [memory]
    return len(result) # 부분집합의 개수

A = list(range(1,13))
T = int(input())
for tc in range(1,T+1):
    n, K = map(int,input().split())
    print(f"#{tc} {subset_bit(A,n)}")