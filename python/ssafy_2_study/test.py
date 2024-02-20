def inorder(T, N):
    global num
    if T <= N:
        inorder(2*T, N)
        visit[T] = num
        num += 1
        inorder(2*T+1, N)
        
for tc in range(1,11):
    N = int(input()) # 글자수
    word_list = ['just zero'] # 노드별 글씨 목록 생성
    visit = [987654321] * (N+1) # 몇번째로 방문하냐 확인 목적

    for _ in range(N):
        temporary_list = list(input().split())
        word_list += [temporary_list[1]] # 각 노드별 단어가 무엇이 있는지 입력

    num = 0
    inorder(1,N)
    cnt = 0
    result = []
    while True:
        result += [word_list[visit.index(cnt)]]
        # n번째(1부터 끝까지)로 방문하는 노드의 인덱스 추출 후 그 인덱스의 글씨가 무엇인지 파악
        cnt += 1
        if cnt == N:
            break

    print(f"#{tc}", end = ' ')
    for m in range(N):
        print(f"{result[m]}", end = '')
    print()

