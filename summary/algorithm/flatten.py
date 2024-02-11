for tc in range(1,11):
    dump = int(input())
    ground_info = list(map(int, input().split()))
    for i in range(dump):
        ground_info.sort()
        ground_info[-1] = ground_info[-1] -1
        ground_info[0] = ground_info[0] + 1

    print(f"#{tc} {max(ground_info) - min(ground_info)}")

