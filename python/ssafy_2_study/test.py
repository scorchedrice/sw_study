<<<<<<< HEAD
'''
연산 트리
inorder탐색해야함
leaf : 피연산자, 그 외 연산자
N을 주고 그 다음에 무엇을 입력할지 준다.
정수인 경우 양의 정수를 주고
연산자라면 해당 노드의 왼쪽자식, 오른쪽 자식의 노드 번호를 준다.
'''
def change_node():
    for k in range(N, 0, -1):
        if type(my_son[k]) == list:
            if node[k] == '-':
                node[k] = node[my_son[k][0]] - node[my_son[k][1]]
            elif node[k] == '+':
                node[k] = node[my_son[k][0]] + node[my_son[k][1]]
            elif node[k] == '/':
                node[k] = node[my_son[k][0]] / node[my_son[k][1]]
            elif node[k] == '*':
                node[k] = node[my_son[k][0]] * node[my_son[k][1]]

for tc in range(1,11):
    N = int(input())       
    # 노드의 수
    node = [0] * (N+1)
    my_son = [0] * (N+1)
    for k in range(N):
        for_node = list(input().split())
        node[int(for_node[0])] = for_node[1]
        if len(for_node) == 3:
            my_son[int(for_node[0])] = [int(for_node[2])]
        elif len(for_node) == 4:
            my_son[int(for_node[0])] = [int(for_node[2]), int(for_node[3])]
    
    for l in range(1,N+1):
        if node[l] != '+' and node[l] != '-' and node[l] != '/' and node[l] != '*':
            node[l] = int(node[l])
    change_node()
    print(f"#{tc} {int(node[1])}")
=======
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

>>>>>>> 56af9e9465aa96b5c4d5f2166d73bb99c24f1a51
