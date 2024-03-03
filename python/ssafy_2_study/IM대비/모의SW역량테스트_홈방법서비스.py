'''
운영비용은 다음과 같이 계산된다.
K**2 + (K-1)**2
운영 비용은 도시 밖으로 벗어난 지역이 있어도 동일하다.
'''
'''
손해를 보지 않으면서, 최대한 많은 집에 서비스를 제공할 수 있는 서비스 영역을 찾자.
이 때 집의 수를 출력하자.
'''
'''
각 좌표별로 구역을 넓히며 집을 센다.
끝까지 넓힌 것 까지 탐색하고, 집의수를 구한다.
이 때 집의 수와 M을 곱해 얻을 수 있는 수익을 구한다.
이를 유지비용을 계산한 후 이 값과 비교해 손해인지 이득인지 판별한다.
이득이라면 최대 집의 수를 갱신한다.
'''
'''
1. 좌표별 구역을 넓히며 집을 세는 함수 정의
    1-1. 함수의 내용엔, 영역을 넓히는 과정
    1-2. 해당 영역에서 집의 개수를 세는 것
        while을 활용해서 함수를 정의하고, 모든 집의 개수와 센 집의 개수가 같으면 정지
    1-3. 손 익을 따지는 과정
    이 포함되어야 한다.
'''
def cal_cost(pivot_i, pivot_j):
    global max_house
    size = 1
    while True:
        cnt_home = 0
        for i in range(-size+1, size):
            for j in range(-size + 1, size):
                if abs(i)+abs(j) < size:    
                    if 0<=pivot_i + i<=N-1 and 0<=pivot_j + j<=N-1:
                        if matrix[pivot_i  + i][pivot_j + j] == 1:
                            cnt_home += 1
        
        # 해당 사이즈의 영역 내 집의 수를 센 후 손익을 따진다.
            
        for_maintain = size**2 + (size-1)**2
        get = cnt_home * M
        if get - for_maintain >= 0:
            # 손해를 보지 않는다면
            if max_house < cnt_home:
                # 그 때 집의 최대 개수를 갱신
                max_house = cnt_home
        size += 1
        if cnt_home == num_home:
            break
    return

T = int(input())
for tc in range(1,T+1):

    N, M = map(int,input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int,input().split())))

    num_home = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                num_home += 1

    max_house = -1
    for i in range(N):
        for j in range(N):
            cal_cost(i,j)

    print(f"#{tc} {max_house}")