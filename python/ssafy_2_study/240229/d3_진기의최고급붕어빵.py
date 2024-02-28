T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    # N : 붕어빵을 살 사람 인원, M초당 K개의 붕어빵 만들기 가능
    arrive_time = list(map(int,input().split()))
    # 손님들이 도착하는 시간대 리스트, 도착 시간은 각각 11,111이하의 값을 가짐
    arrive_time.sort()
    # 먼저 오는 손님 부터
    cake_list = [0]*(N)
    # 손님이 도착했을 때, 만들어 둔 붕어빵의 수를 담을 리스트
    for i in range(N):
        arr_time = arrive_time[i] # i번째 손님의 도착 시간
        cake_list[i] = (arr_time//M) * K # 해당 손님이 왔을 때 가지고 있는 붕어빵 최대개수

    # 판매 시작, 판매량을 계속 누적시키고, 붕어빵 최대개수 - 누적판매량이 음수가 되면 impossible
    total_sell = 0
    for j in range(N):
        if cake_list[j] - total_sell > 0:
            # 현재 가지고 있는 붕어빵의 수 - 누적 판매량이 한개 이상이라면 (판매 가능하면)
            total_sell += 1
        else:
            print(f"#{tc} Impossible")
            break
    else:
        print(f"#{tc} Possible")