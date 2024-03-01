T = int(input())
for tc in range(1,T+1):
    M, A = map(int,input().split())
    # M은 이동시간, A는 충전기의 개수
    move_a = list(map(int,input().split()))
    move_b = list(map(int,input().split())) # A, B의 이동 정보
    charger = []
    for _ in range(A):
        I,J,cover,power = map(int,input().split())
        charger.append((power,I,J,cover,_))
        # 파워, 좌표i, 좌표j, 범위, 충전기 번호
    charger.sort(reverse = True)
    # 파워 순으로 정렬

    A_now = [1,1]
    B_now = [10,10]
    flow = [(0,0),(0,-1),(1,0),(0,1),(-1,0)]

    result = 0
    idx = -1
    while True:
        dist_A = []
        dist_B = []
        # 현 위치에서 접근 가능한 충전기 확인
        for i in range(len(charger)):
            cal_a_dist = abs(A_now[0] - charger[i][1]) + abs(A_now[1] - charger[i][2])
            if cal_a_dist <= charger[i][3]:
                dist_A.append(charger[i])
            cal_b_dist = abs(B_now[0] - charger[i][1]) + abs(B_now[1] - charger[i][2])
            if cal_b_dist <= charger[i][3]:
                dist_B.append(charger[i])
        
        if dist_A != [] and dist_B == []: # A만 사용 가능한 충전기가 있다면
            result += dist_A[0][0]
        elif dist_A == [] and dist_B != []: # B만 사용 가능한 충전기가 있다면
            result += dist_B[0][0]
        elif dist_A != [] and dist_B != []: # A, B 둘 다 모두 충전기에 접근 가능하다면
            max_power = -1
            for a in range(len(dist_A)):
                for b in range(len(dist_B)):
                    if dist_A[a][4] == dist_B[b][4]:
                        # 둘 다 같은 충전기를 골랐다면
                        charge_power = dist_A[a][0]
                    else:
                        # 둘이 다른 충전기를 골랐다면
                        charge_power = dist_A[a][0] + dist_B[b][0]
                    if max_power < charge_power:
                        max_power = charge_power
            result += max_power
        idx += 1
        if idx == M:
            break
        a_flow = move_a[idx]
        b_flow = move_b[idx]
        A_now[0] = A_now[0] + flow[a_flow][0]
        A_now[1] = A_now[1] + flow[a_flow][1]
        B_now[0] = B_now[0] + flow[b_flow][0]
        B_now[1] = B_now[1] + flow[b_flow][1]
    print(f"#{tc} {result}")
