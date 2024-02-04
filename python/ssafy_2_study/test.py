N, M = map(int, input().split())
ricecake_list = list(map(int, input().split()))

height_list = list(range(0,max(ricecake_list))) # 절단기 높이가 될 수 있는 리스트
# 순차탐색
def my_cut(my_list, target, height_list):
    for height_cut in height_list:
        for_result = []
        for i in range(0,len(my_list)):
            if height_cut < my_list[i]: # 절단기의 높이가 떡의 길이보다 낮아야 잘리므로
                for_result += [my_list[i] - height_cut] # 자른것들의 길이 리스트
        if sum(for_result) == target:
            return height_cut

print(my_cut(ricecake_list, M, height_list))
print('순차탐색')

# Binary

def binary_cut(my_list, target, height_list):
    mid_index = len(height_list)//2
    
    for_result = 0
    for i in range(0,len(my_list)):
        if my_list[i] > height_list[mid_index]:
            for_result += my_list[i] - height_list[mid_index]

    if for_result == target:
        return height_list[mid_index]
    elif for_result > target:
        return binary_cut(my_list, target, height_list[mid_index +1:])
    elif for_result < target:
        return binary_cut(my_list, target, height_list[0:mid_index])

print(binary_cut(ricecake_list, M, height_list))
print('순차탐색')