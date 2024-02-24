def cal_subset(arr,n):
    subset_list = [] # 구한 부분집합을 담을 빈 리스트
    for i in range(1<<len(arr)): # 부분집합을 추출할 리스트의 개수
        mid_subset = [] # 부분집합을 담기 위한 중간단계 역할을 할 빈 리스트
        for j in range(len(arr)):
            if i & (1<<j):
                mid_subset += [arr[j]]
        if len(mid_subset) == n and sum(mid_subset) == K:
            subset_list += [mid_subset]
    return subset_list

A = list(range(1,13)) # 1부터 12까지의 자연수로 이루어진 리스트
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    print(f"#{tc} {len(cal_subset(A,N))}")