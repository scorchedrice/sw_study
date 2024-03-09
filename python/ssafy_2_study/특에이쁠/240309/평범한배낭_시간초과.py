'''
N개의 물건, 각각 W의 무게와 V의 가치 (정렬할 필요가 있다면, 앞에 정렬할 필요성이 있는 것을 두고 tuple 혹은 list)
배낭의 물건 담을 수 있는 양 = K
배낭에 넣을 수 있는 물건들 가치의 최댓값 계산할 것

고려해야 할 것 : 무게가 애매하게 남아서, 가치 순으로 넣는 것 보다 하나를 빼고 가치 낮은 것을 여러개 넣는 것이 방법일 수 있다.
'''
import sys

N, K = map(int,input().split())
candidate = []
for _ in range(N):
    candidate.append(list(map(int,input().split())))

mx = -1
def dfs(n,sm,sv):
    global mx
    if sm > K:
        return
    if n == N:
        mx = max(sv, mx)
        return
    dfs(n+1, sm + candidate[n][0], sv + candidate[n][1]) # 택하는 경우
    dfs(n+1, sm, sv) # 택하지 않는 경우
dfs(0,0,0)
print(mx)