'''
직원들 번호, 해야 할 일 1부터 N 넘버링(idx 주의)
i번 직원이 j번 일을 하면 성공할 확률이 P(ij)

주어진 일이 모두 성공할 확률 (확률의 곱)의 최댓값
'''
def dfs(n,percent):
    global mx
    if n == N:
        if percent > mx:
            mx = percent
        return
    if percent * 100**(N-n) <= mx:
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, percent * matrix[n][i])
            v[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int,input().split())))

    mx = -987654321
    v = [0] * N
    dfs(0,1)
    mx = mx * (100**(-(N-1)))
    print(f"#{tc} {mx:.6f}")