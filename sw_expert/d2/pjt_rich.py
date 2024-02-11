# 연속된 N일 동안의 물건 매매가를 예측하여 알고있다.
# 하루에 하나만큼 구매 가능하다.
# 판매는 언제든 가능하다.
# N은 2이상 1,000,000 이하의 자연수
# 각 날의 매매가는 10000이하이다.

'''
매매가 리스트를 입력받고 sort한다.
리스트를 진행하면서 list[-1]을 만나면 모두 판다. ((list[-1] - 현재 구매가)가 0보다 큰 경우 구매)
그 후에 pop()을 하고 다시 max를 구한다.
그리고 동일한 과정을 진행한다.
'''

T = int(input())
for tc in range(1,T+1):
    day = int(input()) # == len(price_list)
    price_list = list(map(int, input().split()))
    pivot_list = [0]*day # 기준이 되는 리스트 미리 작성하기.
    pivot_list[-1] = price_list[-1] 
    
    profit = 0
    
    for i in range(day - 2, -1, -1):
        if pivot_list[i+1] > price_list[i]:    # pivot 보다 작은 값이라면
            pivot_list[i] = pivot_list[i+1]
        else:   # 그게 아니고 pivot보다 큰 값을 발견한다면
            pivot_list[i] = price_list[i]   # pivot을 수정한다.
        
        profit += pivot_list[i] - price_list[i]

    print(f"#{tc} {profit}")    
