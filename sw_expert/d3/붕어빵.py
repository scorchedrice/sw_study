# M초의 시간을 들이면 K개의 붕어빵을 만든다.
# 0초 이후에 손님들이 언제 도착하는지 주어지면, 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램

# 손님들의 도착 시간대는 11,111 이하의 정수고 손님의 수, M, K는 100 이하 1이상이다.
'''
시간대 별로 진기가 만들어 둔 붕어빵의 수를 기록하는 리스트를 작성하고
손님들이 온 시간대에 만들어 둔 붕어빵 리스트의 수에서 뺀다.
이 때 만들어 둔 붕어빵이 없다면 불가능을 출력한다.

마지막 손님까지 붕어빵을 제공할 수 있는 경우 가능을 출력한다.
'''
def cal_my_cake(N, my_cake):
    my_cnt = 0
    for i in range(N):
        # 손님이 한명 도착하면
        my_cnt += 1
        my_cake[i] -= my_cnt # 해당 시간대에 가지고 있던 붕어빵에서 지금까지 받은 손님의 수 만큼 뺀다.
        # 첫손님은 붕어빵 하나 빼고 두번째 손님은 둘 빼고 ...
    
    for _ in my_cake:
        if _ < 0:
            return 'Impossible' # 그 결과 0 미만의 붕어빵이 남은 케이스가 존재한다면.
    else:
        return 'Possible' # 모두 제공했다면


T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split()) # N : 손님의 수, M : K개를 만드는 데 소요되는 시간, K : M초동안 만들 수 있는 붕어빵의 수

    time_list = list(map(int, input().split())) # 도착하는 손님들의 도착 시간대 정보
    time_list.sort() # 빨리 도착하는 순으로 정렬

    # 해당 손님이 도착했을 때, 가지고 있는 붕어빵 개수 리스트 작성
    my_cake = []
    for time in time_list: # 3초에 2개를 만들 수 있고, 5초에 도착한다면 2가 나와야함(5//3)*2
        my_cake += [(time//M)*K]

    print(f"#{tc} {cal_my_cake(N, my_cake)}")