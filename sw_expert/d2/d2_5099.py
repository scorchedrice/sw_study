def f():
    while True:
        for i in range(N):
            if pizza_list == []:
                break
            if oven_info[i] == []:
                oven_info[i] += pizza_list[0]
                del pizza_list[0]
                
        for j in range(N):
            if oven_info[j] == []:
                continue
            oven_info[j][1] = oven_info[j][1]//2
            if oven_info[j][1] == 0:
                oven_info[j] = []
                if len(pizza_list) == 0 and oven_info.count([]) == N-1:
                    return
        
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    C_list = list(map(int, input().split()))
    pizza_list = []
    for k in range(M):
        pizza_list += [[k, C_list[k]]]
    # 첫번째 피자 번호, 두번째 치즈의 양
    oven_info = [[] for _ in range(N)]
    f()
    for k in oven_info:
        if k != []:
            print(f"#{tc} {k[0]+1}")
