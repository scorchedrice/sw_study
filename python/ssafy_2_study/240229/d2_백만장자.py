T = int(input())
for tc in range(1,T+1):
    N = int(input()) # N 굉장히 크기에 계속적인 계산을 방지하도록 식을 세워야함
    price_list = list(map(int,input().split()))
    # 가격은 10,000이하
    max_benefit = [0] * N
    max_price = price_list[-1]
    for k in range(N-1, -1, -1):
        if max_price < price_list[k]:
            max_price = price_list[k]
        max_benefit[k] = max_price - price_list[k]

    result = 0
    for days in range(N):
        result += max_benefit[days]    
    print(f"#{tc} {result}")