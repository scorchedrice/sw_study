from collections import deque

def one_cycle():
    global stack
    while True:
        for k in range(N):
            if oven[k] == 0 and pizza_info != deque():
                oven[k] = deque.popleft(pizza_info)
                # 오븐이 비어있음을 확인했으면, popleft()
                # 빈 오븐에 피자를 넣는 과정
        # 한 바퀴 돌리자
        for l in range(N):
            if oven[l] != 0:
                # 무언가 있는 오븐칸이라면
                oven[l][1] = oven[l][1]//2
                if oven[l][1] == 0:
                    stack += [oven[l]]
                    oven[l] = 0
        if len(stack) == M:
            break
        
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    # 화덕 사이즈 N, 구울 피자 M
    pizza = list(map(int,input().split()))
    pizza_info = deque()
    for k in range(M):
        pizza_info += [[k+1, pizza[k]]]
    oven = [0] * N
    stack = []
    one_cycle()
    print(f"#{tc} {stack[-1][0]}")