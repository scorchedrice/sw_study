def change_alpha(index, cnt, prize_num):
    # 재귀 정지 조건 1. 인덱스, 바꾸는 횟수
    if index >= len(prize_num) or cnt == N:
        ans.append(''.join(prize_num))
        return
    # 재귀 정지 조건 2. 바꿔야 하는 횟수 이전에 최대값을 구한 경우
    # 이 경우엔 cnt와 값을 tuple로 함께 반환한다.
    # 이 값을 토대로 bonus_change 진행
    if int(''.join(prize_num)) == max_prize:
        ans.append((''.join(prize_num),cnt))
        return
    #index를 하나하나 늘려가며 볼건데, 그 이후의 인덱스 중 최대값이 아니라면
    if prize_num[index] != max(prize_num[index:]):
        max_index_list = []
        # 최대 값이 존재하는 인덱스를 찾아야함.
        for l in range(index,len(prize_num)):
            if prize_num[l] == max(prize_num[index:]):
                max_index_list += [l]
        # 최대 값이 있는 인덱스 목록 원소들을 교환하는 모든 경우의 수를 고려하기 위해 재귀
        for k in range(len(max_index_list)):
            cnt += 1 # cnt를 하나 늘리고 자리를 바꾼 뒤 재귀
            prize_num[max_index_list[k]], prize_num[index] = prize_num[index], prize_num[max_index_list[k]]
            change_alpha(index, cnt, prize_num)
            # 초기화
            prize_num[max_index_list[k]], prize_num[index] = prize_num[index], prize_num[max_index_list[k]]
            cnt -= 1
    else: # 만약 해당 인덱스의 값이 그 인덱스 이후의 값 중 가장 큰 값이면 인덱스만 하나 추가하고 재귀
        index += 1
        change_alpha(index, cnt, prize_num)

# 바꿔야 하는 횟수 이전, 최대값을 만들어낸 경우 진행할 함수
def bonus_change(cnt,prize_num_str):
    prize_num = list(prize_num_str)
    while True:
        if cnt == N:
            return ''.join(prize_num)
        if prize_num != list(set(prize_num)): # 중복되는 것 있으면(set로 중복값 확인)
            return ''.join(prize_num) # 중복되는 것 끼리 계속 바꾸면 결국 같은 값이 나오므로
        elif prize_num == list(set(prize_num)): # 중복되는 것이 없으면 끝에것들끼리 계속 바꿔나가면 되므로
            prize_num[-1], prize_num[-2] = prize_num[-2], prize_num[-1]
            cnt += 1

T = int(input())
for tc in range(1,T+1):
    prize, N = input().split()
    N = int(N)
    prize_num = list(prize)
    max_prize = ''.join(sorted(prize_num, reverse = True)) # str값이라 해도 고유의 코드값으로 역순배열된다.
    max_prize = int(max_prize)
    ans = []
    change_alpha(0,0,prize_num) # index 0 , cnt 0 으로 시작한다. 이 함수의 결과로 ans를 받는다.
    ans = list(set(ans)) # 중복 경우의 수 제거
    for i in range(len(ans)):
        if type(ans[i]) == tuple: # 위 함수에서 바꿔야 하는 횟수 이전에 최대값을 도출한 경우 tuple로 값을 반환하기로 약속했으니
            print(f"#{tc} {bonus_change(ans[i][1], ans[i][0])}") # tuple엔 cnt, 그 cnt일 때 상금의 정보가 담겨있다. 이를 bonus_change연산.
            break
    else:
        print(f"#{tc} {max(ans)}")