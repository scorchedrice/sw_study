# 스페이드(S) 다이아몬드(D) 하트(H) 클로버(C) (4)
# 각각 A(01), 2~10(02~10), J(11), Q(12), K(13)
# 총 4*13 = 52장의 카드
'''
겹치는 카드를 가지고 있으면 : 오류
영준이는 몇장의 카드를 가지고 게임을 시작한다.
몇장의 카드가 더 있어야 게임을 시작할 수 있나
'''


T = int(input())
for tc in range(1,T+1):
    S = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
    D = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
    H = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
    C = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
    card = input()
    card_list = [card[i:i+3] for i in range(0,len(card),3)]
    error_check = False
    for card_info in card_list:
        try:
            if card_info[0] == 'S':
                S.remove(card_info[1:])
            elif card_info[0] == 'D':
                D.remove(card_info[1:])
            elif card_info[0] == 'H':
                H.remove(card_info[1:])
            elif card_info[0] == 'C':
                C.remove(card_info[1:])
        except ValueError:
            print(f"#{tc} ERROR")
            error_check = True
            break
    if error_check == False:
        print(f"#{tc} {len(S)} {len(D)} {len(H)} {len(C)}")