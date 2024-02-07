import math

N = 4
tile_accum_list = [0]*(1001) # 임의의 리스트 생성
tile_accum_list[1] = 1
tile_accum_list[2] = 3

if N >= 3:
    for i in range(3,N+2):
        my_cnt = 0
        a = i+1
        b = -1
        if i % 2 == 0:
            while a != b:
                a -= 1
                b += 1
                tile_accum_list[i] += (2**my_cnt)*math.comb(a,b)
                my_cnt += 1
                if a == b:
                    break
        else:
            while a != b:
                a -= 1
                b += 1
                tile_accum_list[i] += (2**my_cnt)*math.comb(a,b)
                my_cnt += 1
                if a-b == 1:
                    break

print(tile_accum_list[N])