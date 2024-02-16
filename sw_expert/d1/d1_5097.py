T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    # N은 숫자의 갯수, M은 과정을 반복하는 횟수
    num_list = list(map(int, input().split()))
    num_list += [0] * M
    # 0으로 구성된 리스트를 추가하여 리스트 삭제 등의 과정 불필요하도록
    for k in range(M):
        # M번 과정을 반복한다.
        num_list[k + N] = num_list[k]
    print(f"#{tc} {num_list[-N]}")

