'''
좌표 1부터 N까지 총 N개의 꽃이 있다. (인덱스 주의)
x에 위치한 자동 분무기는 x-D 이상 x+D이하의 범위에 물을 뿌린다. (D는 자동 분무기 성능)
N과 D가 주어진 경우 모든 꽃이 물을 받을 수 있도록 하기 위한 최소한의 분무기 수 구하기
'''

T = int(input())
for tc in range(1,T+1):
    N, D = map(int,input().split())
    # 꽃의 수 N, 분무기 성능 D
    '''
    성능이 1이라면, 범위는 3
    성능이 2이라면, 범위는 5
    성능이 3이라면, 범위는 7

    즉, 2*성능 + 1이 물을 뿌릴 수 있는 범위다.
    '''
    cover = 2*D + 1
    cnt = 0
    now_cover = 0
    while True:
        now_cover += cover
        cnt += 1
        if now_cover >= N:
            break
    print(f"#{tc} {cnt}")