# 각 숫자는 자리수에 해당함
# ex 8 8 8 3 2 : 88832
def change_alpha(index, cnt, prize_num):
    if index >= len(prize_num) or cnt == N:
        ans.append(''.join(prize_num))
        return
    if int(''.join(prize_num)) == max_prize:
        ans.append((''.join(prize_num),cnt))
        return
    if prize_num[index] != max(prize_num[index:]):
        max_index_list = []
        for l in range(index,len(prize_num)):
            if prize_num[l] == max(prize_num[index:]):
                max_index_list += [l]
        for k in range(len(max_index_list)):
            cnt += 1
            prize_num[max_index_list[k]], prize_num[index] = prize_num[index], prize_num[max_index_list[k]]
            change_alpha(index, cnt, prize_num)
            prize_num[max_index_list[k]], prize_num[index] = prize_num[index], prize_num[max_index_list[k]]
            cnt -= 1
    else:
        index += 1
        change_alpha(index, cnt, prize_num)

def bonus_change(cnt,prize_num_str):
    prize_num = list(prize_num_str)
    while True:
        if cnt == N:
            return ''.join(prize_num)
        if prize_num != list(set(prize_num)): # 중복되는 것 있으면
            return ''.join(prize_num)
        elif prize_num == list(set(prize_num)):
            prize_num[-1], prize_num[-2] = prize_num[-2], prize_num[-1]
            cnt += 1

T = int(input())
for tc in range(1,T+1):
    prize, N = input().split()
    N = int(N)
    prize_num = list(prize)
    max_prize = ''.join(sorted(prize_num, reverse = True))
    max_prize = int(max_prize)
    ans = []
    change_alpha(0,0,prize_num)
    ans = list(set(ans)) # 중복 경우의 수 제거
    for i in range(len(ans)):
        if type(ans[i]) == tuple:
            print(f"#{tc} {bonus_change(ans[i][1], ans[i][0])}")
            break
    else:
        print(f"#{tc} {max(ans)}")