def find_parent(x):
    if group[x] == x:
        return x
    else:
        group[x] = find_parent(group[x])
    return group[x]
 
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return
    
    if a<b:
        group[b] = a
    
    else:
        group[a] = b
     
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    group = [0] * (N+1)
    for k in range(1,N+1):
        group[k] = k

    for i in range(M):
        A = lst[i*2]
        B = lst[i*2 + 1]
        union(A,B)
         
    ans = [0] * N
    for i in range(1,N+1):
        ans[i-1] = find_parent(i)
        # union은 상위 단계가 무엇인지만 연결해줌!!!!! 부모를 완전 찾기위해선
        # 전 범위를 대상으로 부모를 정확하게 하는 과정이 필요!
    print(f"#{tc} {len(set(ans))}")