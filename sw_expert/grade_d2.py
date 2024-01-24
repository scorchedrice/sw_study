T = int(input())
for a in range(0,T):
    N, K = list(map(int, input().split()))
    #len_height = []
    count = 0
    for_height_info = []
    for j in range(0,N):
        width_info = list(map(int, input().split()))
        for_height_info.extend([width_info])
        width_detail = [width_info[0]]
        width_group = []
        for k in range(1,N):
            if width_info[k] == width_info[k-1]:
                width_detail += [width_info[k]]
            elif width_info[k] != width_info[k-1]:
                width_group += [width_detail]
                width_detail = [width_info[k]]
        width_group += [width_detail]
        width_info = []
        for l in range(0, len(width_group)):
            if width_group[l][0] == 1:
                width_info += [width_group[l]]
        len_width = []
        for m in range(0, len(width_info)):
            len_width += [len(width_info[m])]
        for n in len_width:
            if K == n:
                count = count + 1
    #---------------------여기까지 width 정보와 칸 세기
    height_list = []
    for j in range(0, N):
        height_detail = []
        for l in range(0, N):
            height_detail = height_detail + [for_height_info[l][j]]
        height_list = height_list + [height_detail]

    for j in range(0,N):
        height_info = height_list[j]
        height_detail = [height_info[0]]
        height_group = []
        for k in range(1,N):
            if height_info[k] == height_info[k-1]:
                height_detail += [height_info[k]]
            elif height_info[k] != height_info[k-1]:
                height_group += [height_detail]
                height_detail = [height_info[k]]
        height_group += [height_detail]
        height_info = []

        for l in range(0, len(height_group)):
            if height_group[l][0] == 1:
                height_info += [height_group[l]]
        len_height = []
        for m in range(0, len(height_info)):
            len_height += [len(height_info[m])]
        for n in len_height:
            if K == n:
                count = count + 1
    print(f"#{a+1} {count}")
