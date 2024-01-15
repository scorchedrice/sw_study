T = int(input())
for test_case in range(1, T + 1):
    item_number = int(input())
    price_list = list(map(int, input().split()))
    buy_list = []
    for i in range(0, item_number):
        if price_list[i] > price_list[i+1]:
            pass
        elif price_list[i] == price_list[i+1]:
            buy_list.apend()
        else:
            plus_list = price_list[i+1] * len(buy_list)
            plus = sum(plus_list - buy_list)         
print(plus)
            