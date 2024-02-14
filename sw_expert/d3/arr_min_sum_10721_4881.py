def my_sum(i,k,s):
    global min_value
    if i == k:
        s = 0
        for j in range(k):
            s += matrix[j][P[j]]
        if min_value > s:
            min_value = s
    elif min_value <= s:
        return
    else:
        for l in range(i,k):
            P[i] ,P[l] = P[l], P[i]
            my_sum(i+1,k,s+matrix[i][P[i]])
            P[i] ,P[l] = P[l], P[i]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    P = list(range(N))
    matrix = []
    for _ in range(N):
        matrix += [list(map(int, input().split()))]
    min_value = 100
    my_sum(0,N,0)
    print(f"#{tc} {min_value}")
