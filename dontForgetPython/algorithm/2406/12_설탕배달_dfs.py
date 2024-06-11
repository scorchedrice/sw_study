# dfs로 풀어보기
weight = int(input())

def dfs(n,three_bag,five_bag):
    global min_bag
    
    if n == 2:
        # print(three_bag, five_bag)
        # dfs함수 반복에 의해 바구니 두개의 값이 정해진 경우
        if 3*three_bag + 5*five_bag == weight:
            if (three_bag+five_bag) < min_bag:
                min_bag = three_bag+five_bag
        return
    for i in range(0,(weight//3)+1):
        # 반복문을 실행할건데 바구니가 차있는 것을 확인하는 과정을 거치고 진행
        if n == 0:
            # 3킬로 가방을 아직 채우지 않음.
            dfs(1,i,-1)
        elif n == 1:
            # 3킬로 가방을 채움
            dfs(2,three_bag,i)


# 바구니 갯수 최소값 초기값 설정
min_bag = 987654321
dfs(0,-1,-1)
if min_bag != 987654321:
    print(min_bag)
else:
    print(-1)
