# Greedy
# 3-1 거스름돈
# 카운터에 있는 잔돈 : 500, 100, 50, 10 원 동전
# N원을 거슬러 줘야 할 때 줘야 할 동전의 최소 개수 (N은 항상 10의 배수)

def count_coin(n):
    '''
    n원을 줘야할 때, 500, 100, 50, 10 원의 동전을 최소한으로 사용하여 지급하는 경우
    '''
    coin_list = [500, 100, 50, 10]
    count_coin = 0
    for coin in coin_list:
        a = n//coin
        n = n-a*coin
        count_coin = count_coin + a
    return count_coin

print(count_coin(1260), ': this is 3-1 answer')

# 3-2 큰 수의 법칙
# M개의 수를 더하는데, 동일 수는 K번 초과하여 더해질 수 없다.
# N개의 자연수를 활용한다.
# index가 다른 경우 다른 수 취급
# N : 2이상 1000이하, M 1이상 10000이하, K 1이상 10000이하 자연수
# 각 자연수는 공백으로 구분
# 첫째 줄 : N M K
# 둘째 줄 : 자연수 목록 (자연수는 1 이상 10000이하)
# K <= M
# 가장 큰 수 !
'''
5 8 3
2 4 5 4 6

46
'''
'''
list_NMK = list(map(int, input().split())) # N, M, K 리스트
list_int = list(map(int, input().split())) # 주어지는 자연수 목록 리스트
list_int.sort() # 주어진 자연수 목록 리스트를 작은 수부터 큰수로 정렬
def dongbin(): # 동빈이의 큰 수의 법칙 함수 정의
    overall = list_NMK[-2] # M
    max_repeat = list_NMK[-1] # K
    count = 0 # 몇 회 반복했는지 계산 위해 (while의 정지 조건 설정 목적)
    answer = 0 # dongbin()의 return 값 계산 위해
    while count != overall:
        answer = answer + max_repeat * list_int[-1] # 가장 큰 수를 max_repeat 만큼 더하고
        count = count + max_repeat * 1
        answer = answer + list_int[-2] # 그 후에 그보다 작은 수를 한번 더하고 이를 반복
        count = count + 1
    return answer
print(dongbin(), ': this is 3-2 answer')
'''
# 3-3 숫자 카드 게임
# 여러 개의 카드 중 가장 높은 숫자가 쓰인카드 한장을 뽑는 게임
# 게임의 룰
'''
N * M 형태로 놓여 있다
N은 행, M은 열
1. 행을 선택 (뽑을 목적의)
2. 거기서 그 행의 가장 낮은 수 뽑기
즉, 그 행에서 가장 낮은 수가 최대한 큰 수가 나오도록 해야함
'''
'''
3 3
3 1 2
4 1 4
2 2 2

첫째 줄에 N * M 인지 입력
이후 카드의 숫자 입력
'''
'''
game_size = list(map(int, input().split())) # 카드 게임의 규모 리스트화 [N, M]
card_data = []
card_min = []
for i in range(0, game_size[0]):
    card_data = card_data + [list(map(int, input().split()))] # N번 데이터를 입력받고 이를 리스트 안의 리스트화
    card_min.append(min(card_data[i])) # 한번 입력받은 한 행의 리스트들 중 최소값을 리스트화

print(max(card_min), 'this is 3-3 answer') # 각 행의 min 값 중 가장 큰 값 도출
'''
