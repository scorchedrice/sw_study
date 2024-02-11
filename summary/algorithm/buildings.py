'''
for tc in range(1,11):
    N = int(input())
    building_info = list(map(int, input().split()))
    building_map = [[0]*N for _ in range(max(building_info))]

    for j in range(N):
        for i in range(building_info[j]):
            building_map[i][j] = 1

    count = 0
    for i in range(len(building_map)):
        for j in range(2,N-2):
            if building_map[i][j] != 0:
                if building_map[i][j-2] == 0 and building_map[i][j-1] == 0 and building_map[i][j+1] == 0 and building_map[i][j+2] == 0:
                    count += 1

    print(f"#{tc} {count}")
'''
for tc in range(1,11):
    N = int(input())
    building_info = list(map(int, input().split()))

    count = 0
    for i in range(2,N-2):
        height_info = building_info[i-2:i+3]
        height_info.sort()
        if height_info[-1] == building_info[i]:
            count = count + (height_info[-1]-height_info[-2])

    print(f"#{tc} {count}")