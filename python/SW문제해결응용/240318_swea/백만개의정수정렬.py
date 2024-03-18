def qsort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[pivot] >= arr[left]: # end에 도달할 때 까지
            left += 1
        while right > start and arr[pivot] <= arr[right]:
            right -= 1
        
        if left>right: # 둘이 역전된 경우
            arr[pivot], arr[right] = arr[right], arr[pivot]
            # 역전이 되면 이를 pivot과 right를 바꾼다. 이후 while 조건을 충족하지 않아 while 이후의 재귀를 실행한다.
        else: # 역전되지 않은 경우
            arr[left], arr[right] = arr[right], arr[left]
        
    qsort(arr, start, right-1) # 좌측
    qsort(arr, right+1, end) # 우측

arr = list(map(int,input().split()))
qsort(arr,0,1000000-1)
print(arr[500000])