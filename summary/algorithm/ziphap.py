'''
arr = [-7,-5,2,3,8,-2,4,6,9]

n = len(arr)
result = []

for i in range(1<<n):
    for_result = []
    count = 0
    for j in range(n):
        if i & (1<<j):
            count += arr[j]
            for_result += [arr[j]]
    if sum(for_result) == 0:
        result += [for_result]

print(result)
'''
list_A = list(range(1,13))
n = len(list_A)
T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())

    result = []
    for i in range(1<<n):
        count = []
        for j in range(n):
            if i & (1<<j):
                count += [list_A[j]]
        if len(count) == N and sum(count) == K:
            result += [count]
    print(f"#{tc} {len(result)}")