'''
가로의 길이는 항상 1000이하로 주어진다.
각 빌딩의 높이는 최대 255
맨 왼쪽, 오른쪽 두칸씩은 건물 없다
'''
def check_view(building_map):
    cnt = 0
    for k in building_map:
        for l in range(N):
            if k[l] == 1:
                if k[l-2] == 0 and k[l-1] == 0 and k[l+1] == 0 and k[l+2] == 0:
                    cnt += 1
    return cnt

for tc in range(1,11):
    N = int(input())
    buildings = list(map(int,input().split()))
    building_map = []
    
    for k in range(0,255):
        building_map += [[0]*N]
    
    for l in range(N):
        for m in range(buildings[l]):
            building_map[m][l] += 1

    print(check_view(building_map))