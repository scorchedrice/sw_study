T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    num_list.sort()
    result = []
    for i in range(N//2):
        result += [num_list[-(i+1)]] + [num_list[i]]
    if len(num_list) % 2 == 1:
        result += [num_list[N//2]]
    print(f"#{tc}", end = ' ')
    cnt = 0
    for k in result:
        print(k, end = ' ')
        cnt += 1
        if cnt == 10:
            break
    print()