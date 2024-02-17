# 연속된 N일 동안의 물건 매매가를 예측하여 알고있다.
# 하루에 하나만큼 구매 가능하다.
# 판매는 언제든 가능하다.
# N은 2이상 1,000,000 이하의 자연수
# 각 날의 매매가는 10000이하이다.

T = int(input())
for tc in range(1,T+1):
    day = int(input()) # == len(price_list)
    price_list = list(map(int, input().split()))
    pivot_list = [0]*day # 기준이 되는 리스트 미리 작성하기.
    pivot_list[-1] = price_list[-1] 
    profit = 0
    
    for i in range(day - 2, -1, -1):
        if pivot_list[i+1] < price_list[i]:    # pivot 보다 큰 가격이라면
            pivot_list[i] = price_list[i]   # pivot을 수정한다.
        else:   # 그게 아니면
            pivot_list[i] = pivot_list[i+1]
        
        profit += pivot_list[i] - price_list[i]

    print(f"#{tc} {profit}")
