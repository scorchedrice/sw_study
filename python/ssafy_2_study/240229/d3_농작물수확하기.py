'''
0행부터 일단 시작하자.
0행의 중앙에서 우측 하단으로 뻗는 i,j
0행의 중앙에서 좌측 하단으로 뻗는 i,j를 구한다.
이 값들이 벽에 도달하면 그 지점부터 방향을 꺾어 바닥을 향하므로 이를 고려해 index를 추가해 리스트를 형성한다.
'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    my_index_right = [(0,N//2)]
    my_index_left = [(0,N//2)]
    cnt_right = 0
    for right in range((N//2)+1, N):
        cnt_right += 1
        my_index_right += [(cnt_right, right)]

    for right_rev in range(N-2, N//2, -1):
        cnt_right += 1
        my_index_right += [(cnt_right, right_rev)]

    cnt_left = 0
    for left in range((N//2)-1, -1,-1):
        cnt_left += 1
        my_index_left += [(cnt_left, left)]

    for left_rev in range(1, N//2):
        cnt_left += 1
        my_index_left += [(cnt_left, left_rev)]

    my_index_left += [(N-1, N//2)]
    my_index_right += [(N-1, N//2)]

    matrix = []
    for _ in range(N):
        matrix += [list(map(int,input()))]
    result = 0
    for k in range(N):
        result += sum(matrix[k][my_index_left[k][1]:my_index_right[k][1]+1])
    print(f"#{tc} {result}")