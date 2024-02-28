'''
N : 1이상 개큰거 이하 (계속 연산되는 것 방지)
'''
def check_str_to_int(str_num):
    if str_num == '1':
        return 1
    elif str_num == '2':
        return 2
    elif str_num == '3':
        return 3
    elif str_num == '4':
        return 4
    elif str_num == '5':
        return 5
    elif str_num == '6':
        return 6
    elif str_num == '7':
        return 7
    elif str_num == '8':
        return 8
    elif str_num == '9':
        return 9
    elif str_num == '0':
        return 0
    
T = int(input())
for tc in range(1,T+1):
    num_cnt = [0] * 10 # 0,1,2,....10
    N = int(input())
    now = N
    while True:
        tmp = list(str(now))
        for num in tmp:
            check = check_str_to_int(num)
            # print(check)
            if num_cnt[check] == 0:
                num_cnt[check] += 1
            else:
                continue
        if num_cnt == [1,1,1,1,1,1,1,1,1,1]:
            break
        now += N
    print(f"#{tc} {now}") 