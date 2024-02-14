def my_perm(arr,r):
    result = []
    if r == 0:
        return [[]]
    for i, elem in enumerate(arr):
        for P in my_perm(arr[:i] + arr[i+1:], r-1):
            result += [[elem]+P]
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix += [list(map(int, input().split()))]
    P = list(range(N))
    nPn = my_perm(P,N)
    min_value = 100
    for i in range(len(nPn)):
        my_sum = 0
        for j in range(N):
            my_sum += matrix[j][nPn[i][j]]
            if my_sum >= min_value:
                break
        if my_sum < min_value:
            min_value = my_sum
    print(f"#{tc} {min_value}")
    