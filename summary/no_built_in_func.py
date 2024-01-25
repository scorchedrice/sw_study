# min, max
# for 문을 사용, 임의의 값을 max or min으로 지정한 후 index별 숫자와 비교하여 도출

#Example
scores1 = [30, 60, 90, 70]
def max_score(num_list):
    max_value = num_list[0]
    for num in num_list:
        if num > max_value:
            max_value = num
    return max_value

def min_score(num_list):
    min_value = num_list[0]
    for num in num_list:
        if num < min_value:
            min_value = num
    return min_value


print(max_score(scores1))
print(min_score(scores1))

# 중간값 찾기(sort없이 정렬하기)
# Example (SWEA, 2063)
num_list = [85, 72, 38, 80, 69, 65, 68, 96, 22]
# 리스트는 총 홀수개의 숫자로 이루어져 있음.
middle_index = len(num_list)//2 # 중간값은 정렬된 리스트의 middle_index에 위치한다.

# 위에서 구한 min_value 함수 활용해 sort하는 과정
def sort_func(num_list):
    sort_list = []
    for i in range(0, len(num_list)):
        sort_list += [min_score(num_list)]
        num_list.remove(min_score(num_list))
    return sort_list
sorted_list = sort_func(num_list)
print(sorted_list) # sort된 리스트
print(sorted_list[middle_index]) # 중간값

# 현재 리스트의 역방향으로 리스트된 리스트 생성하기 reverse 사용 X
def my_reverse(num_list):
    my_list = [0]*len(num_list) # 0으로 구성된 list 생성
    for i in range(0,len(num_list)):
        my_list[i] = num_list[(-1-i)]
    return my_list
num_list = [85, 72, 38, 80, 69, 65, 68, 96, 22]
print(my_reverse(num_list))

# len 구하기 (len함수 사용 X)
def my_len(num_list):
    len = 0
    for index in num_list:
        len += 1
    return len
print(my_len(num_list))

# count 없이 해당 값 몇번 나왔는지 세어보기, index 추출하기, 8을 가정해보자
num_list = [10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3]
def my_index(num_list, target_num):
    where_num = []
    for index in range(0,len(num_list)):
        if num_list[index] == target_num:
            where_num.append(index)
    return where_num
print(my_index(num_list, 8)) # 8(target number)이 존재하는 num_list의 index

def count_num(num_list, target_num):
    count = 0
    for num in num_list:
        if target_num == num:
            count += 1
    return count
print(count_num(num_list, 8)) # 몇번 나오냐

# 최빈수 구하기
num_list = [10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3]