def qsort(start, end):
    global arr
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right: #left, right가 역전된다면 반복 종료
        # left 를 하나씩 늘리며 탐색하는 과정
        while left <= end and arr[pivot] >= arr[left]:
            # left를 idx로 가지는 arr값이 기준값보다 작으면 반복해라
            left += 1
        while right > start and arr[pivot] <= arr[right]:
            # right를 idx로 가지는 arr값이 기준값보다 크다면 반복해라
            right -= 1
        # left, right가 결정 된 뒤 이들의 관계에 따라 다음의 조치 진행
        if left > right: # 역전된경우
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else: # 역전이 아닌 경우
            arr[left], arr[right] = arr[right], arr[left]
    # 가장 큰 범위를 포함하는 while이 깨졌다 == 역전되었다
            # right를 기준으로 좌 우 qsort진행
    qsort(start, right-1)
    qsort(right+1, end)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    qsort(0,N-1)
    print(f"#{tc} {arr[N//2]}")