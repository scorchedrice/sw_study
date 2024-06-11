# 굉장히 오래걸림. 원과 좌표의 관계, 접하냐 접하면 접점이 몇개냐
from math import sqrt
testcase = int(input())
for tc in range(testcase):
    x1, y1, r1, x2, y2, r2 =  map(int,input().split())

    if x1 == x2 and y1 == y2:
        # 좌표가 동일한 경우
        # 거리가 같다면 무한, 다르다면 0
        if r1 == r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    else:
        # 좌표가 다른 경우 거리를 비교해야 한다.
        sum_r = (r1+r2)**2
        dif_r = (abs(r1-r2))**2
        dif_coord = (x1-x2)**2 + (y1-y2)**2

        # Case1. 외부 한 점에서 접하는 경우
        if sum_r == dif_coord:
            print(1)
            continue
        # Case2. 그냥 멀리 떨어져서 안만나는경우
        elif sum_r < dif_coord:
            print(0)
            continue
        else:
            # Case3. 내부 한 점에서 접하는 경우
            if r1 > r2:
                # r1이 더 큰 경우
                if sqrt(dif_coord) + r2 == r1:
                    print(1)
                    continue
                elif sqrt(dif_coord) + r2 < r1:
                    print(0)
                    continue
            elif r1 < r2:
                # r2 가 더 큰 경우
                if sqrt(dif_coord) + r1 == r2:
                    print(1)
                    continue
                elif sqrt(dif_coord) + r1 < r2:
                    print(0)
                    continue
        print(2)
        
