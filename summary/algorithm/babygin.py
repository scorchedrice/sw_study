card_list = list(range(1,10))
T = int(input())
for tc in range(1,T+1):
    my_card = list(map(int, input()))
    card_count = [0]*10
    for card_num in my_card:
        for card_type in card_list:
            if card_num == card_type:
                card_count[card_type] += 1

    run_cnt = 0
    triplet_cnt = 0
    for i in range(0,len(card_count)):
        if card_count[i] == 6: # 단 하나의 숫자로 조건을 만족하는 경우 triplet 두번
            triplet_cnt += 2
            card_count[i] = card_count[i] -6
            break
        elif card_count[i] >= 3:
            triplet_cnt += 1
            card_count[i] = card_count[i] -3

    for j in range(0,len(card_count)-2):
        if card_count[j] ==2 and card_count[j+1] == 2 and card_count[j+2] == 2:
            run_cnt += 2
            break
        elif card_count[j] >=1 and card_count[j+1] >= 1 and card_count[j+2] >= 1:
            card_count[j] -= 1
            card_count[j+1] -= 1
            card_count[j+2] -= 1
            run_cnt += 1

    if triplet_cnt + run_cnt == 2:
        print(f"#{tc} Baby Gin")
    else:
        print(f"#{tc} Lose")
