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