T= int(input())
for tc in range(1,T+1):

    N, Q = map(int,input().split())
    # 1번부터 N까지의 N개의 상자를 가지고 있음.
    # Q번 작업을 실시한다. 실시 내용은 아래와 같다.
    '''
    i번째(1번째부터 Q번째 작업까지) 작업을 수행할 때
    L번 상자부터 R번 상자까지의 값을 i로 변경한다.
    '''
    # N,Q의 범위가 10**3 이하로 굉장히 크기에, 리스트를 미리 만들고 작업 진행시키기

    box_list = [0] * (N+1) # 인덱스와 연관 시키기 위해 맨 앞 임의의 값 추가
    for box_change in range(1,Q+1):
        L, R = map(int,input().split())
        for _ in range(L, R+1):
            box_list[_] = box_change

    print(f"#{tc}", end = ' ')
    print(*box_list[1:])
