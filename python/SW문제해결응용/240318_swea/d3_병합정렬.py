def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

def change_cnt(left, right):
    global cnt
    num_l = left[-1]
    num_r = right[-1]
    if num_l > num_r:
        cnt += 1
    
def merge(left, right):
    change_cnt(left, right)
    result = [0] * (len(right) + len(left))
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <  right[j]:
            result[i+j] = left[i]
            i += 1
        else:
            right[j] < left[i]
            result[i+j] = right[j]
            j += 1
    while i < len(left):
        result[i+j] = left[i]
        i += 1
    while j < len(right):
        result[i+j] = right[j]
        j+=1
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    lst = merge_sort(lst)
    print(f"#{tc} {lst[N//2]} {cnt}")