def quick_sort(list):
    if len(list) <= 1:
        return list
    
    pivot = list[0]
    tail = list[1:]

    left_side = [num for num in tail if num <= pivot]
    right_side = [num for num in tail if num > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

N, K = map(int, input().split()) # N, K, A, B를 받는 과정
list_A = quick_sort(list(map(int, input().split())))
list_B = quick_sort(list(map(int, input().split())))

for k in range(K): # K번 스와핑 가능하므로 K번 수행
    list_A[k], list_B[(N-1)-k] = list_B[(N-1)-k], list_A[k] # quick_sort 한 A의 첫째 항(min)과 B의 마지막 항(max)를 스와핑

result = 0
for num in list_A:
    result = result + num
print(result)