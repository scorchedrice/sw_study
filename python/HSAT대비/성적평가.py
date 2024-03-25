import sys
N = int(input())
total = [0] * N
score1 = list(map(int,input().split()))
score2 = list(map(int,input().split()))
score3 = list(map(int,input().split()))
for k in range(N):
    total[k] += score1[k] + score2[k] + score3[k]

def CAL_RANK(lst):
    pivot = []
    ans = [0]*N
    for k in range(N):
        pivot.append((lst[k],k))
    pivot.sort(reverse = True)
    ans[pivot[0][1]] = 1
    cnt = 1
    for l in range(1,N):
        if pivot[l][0] == pivot[l-1][0]:
            ans[pivot[l][1]] = cnt
        else:
            cnt = l+1
            ans[pivot[l][1]] = cnt
    print(*ans)
CAL_RANK(score1)
CAL_RANK(score2)
CAL_RANK(score3)
CAL_RANK(total)