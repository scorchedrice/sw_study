def carrot_list_div(carrot_list):
    semi_result = [carrot_list[0]]
    for i in range(1,N):
        if carrot_list[i-1] == carrot_list[i]:
            semi_result += [carrot_list[i]]
        else:
            semi_result += [999] # 숫자가 다른 것 사이에 장벽
            semi_result += [carrot_list[i]]
    
    my_and_list = [] # 숫자가 다른것들을 분리하기 위해
    for index in range(0,len(list(semi_result))):
        if semi_result[index] == 999:
            my_and_list += [index]
    # and index를 활용하여 두개를 뽑는다 (3개의 덩어리 구성)
    result = []
    for i in range(len(my_and_list)):
        and_1 = my_and_list[i]
        for j in range(i+1, len(my_and_list)):
            and_2 = my_and_list[j]

            left = 0
            mid = 0
            right = 0
            for num_index in range(len(semi_result)):
                if num_index < and_1:
                    if semi_result[num_index] != 999:
                        left += 1
                elif and_1 < num_index < and_2:
                    if semi_result[num_index] != 999:
                        mid += 1
                elif and_2 < num_index:
                    if semi_result[num_index] != 999:
                        right += 1
                else:
                    continue
            if left <= N//2 and mid <= N//2 and right <= N//2:
                a = left - mid
                if a < 0:
                    a = mid - left
                b = left - right
                if b < 0:
                    b = right - left
                c = mid - right
                if c < 0:
                    c = right - mid
                result += [list(set([a,b,c]))]
    
    if result == []:
        return -1
    my_result = []
    for m in range(len(result)):
        if len(result[m]) == 1:
            return 0
        else:
            my_result += [max(result[m])-min(result[m])]
    print(my_result)
    return min(my_result)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    carrot_list = list(map(int, input().split()))
    carrot_list.sort()
    print(f"#{tc} {carrot_list_div(carrot_list)}")