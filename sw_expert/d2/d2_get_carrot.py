'''
문제 전략
수레에 실려있는 당근들을 새로운 리스트 혹은 값으로 임의 지정한다.
당근을 하나씩 수레에 넣고, 그 수치가 수레에 꽉 차면 처음으로 간다.
하지만, 수레에 꽉 차기 전 해당 구역의 당근이 모두 수확되었다면
다음칸으로 넘어가 해당 작업을 진행한다.

이동할 때 마다 distance에 수치를 추가하여 결론을 도출한다.
'''

T = int(input())
for tc in range(1,T+1):
    N, M=map(int, input().split())
    # N은 당근을 수확할 수 있는 구역의 수
    # M은 수레에 꽉 차기위한 당근의 수
    # 0번구역에 수레와 창고가 존재한다.

    matrix = [0] + list(map(int,input().split()))

    distance = 0
    current = 0
    my_cart = 0

    while current <= N:
        if matrix[current] == 0:
            current += 1
            distance += 1
            continue

        while matrix[current] != 0 and my_cart != M:
            my_cart += 1
            matrix[current] = matrix[current] - 1
                
        if my_cart == M:
            distance += current
            current = 0
            my_cart = 0
    
        if my_cart != M and matrix == [0] + [0]*N:
            distance += (current-1)

    print(f"#{tc} {distance}")
