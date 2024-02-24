T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int,input().split()))

    total_list = []
    now = 0
    cnt = 1
    my_sum = C[0]
    while True:
        if 0<=now+1<=N-1:
            if C[now] < C[now+1]:
                now += 1
                cnt += 1
                my_sum += C[now]
            elif C[now] >= C[now+1]:
                if cnt >= 2:
                    total_list += [(cnt, my_sum)]
                now += 1
                my_sum = C[now]
                cnt = 1
        else:
            if cnt >= 2:
                total_list += [(cnt, my_sum)]
            break
        

    num_stem = len(total_list)

    max_total = 0
    max_len = 0
    for l in total_list:
        if max_len < l[0]:
            max_len = l[0]
    for m in total_list:    
        if m[0] == max_len:
            if max_total < m[1]:
                max_total = m[1]

    print(f"#{tc} {num_stem} {max_total}")