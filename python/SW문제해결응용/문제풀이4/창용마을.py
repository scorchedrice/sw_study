def find_parent(x):
    if x == parents[x]:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parents[b] = a
    else:
        parents[a] = b

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    parents = list(range(N+1))
    for _ in range(M):
        A, B = map(int,input().split())
        union(A,B)
    ans = [0] * N
    for i in range(1,N+1):
        ans[i-1] = find_parent(i)
    print(f"#{tc} {len(set(ans))}")        
