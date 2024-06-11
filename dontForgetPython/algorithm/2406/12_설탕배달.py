weight = int(input())
# 5kg으로 나누기 시도

five_bag = weight//5 # 일단 나눠봐!
while True:
    if five_bag == 0:
        # 5kg의 덩어리로 들 수 없는 경우 다음으로 넘겨
        break
    else:
        # 5킬로로 들 수는 있는 경우에
        left = weight - 5*five_bag
        # 남은 양은 이정도
        if left == 0:
            # 5킬로로 모든 것을 해결한 경우
            weight = 0
            break
        elif left%3 == 0:
            # 3의 배수가 남은 경우
            weight = left
            # 남은 값을 그대로 넘기는 것이 최소일 것임
            break
        else:
            five_bag = five_bag - 1
            # 일단 덩어리 하나 줄이고 3으로 쪼갤 수 있는지 반복문을 통해 확인

three_bag = weight//3
weight = weight - three_bag*3

if weight == 0:
    print(five_bag + three_bag)
else:
    print('-1')
