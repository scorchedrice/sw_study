T = int(input())
 
 
# 만약 루트가 존재한다면
# 트리를 조호할 수 있는 연결 순서를 저장한다.
def make_tree(start, N):
    while start < N:
        start += 1
        if start % 2 == 0:
            tree[start // 2][0] = start
        elif start % 2 == 1:
            tree[start // 2][1] = start
 
 
def save_num(root):
    global cnt
    if cnt == N:
        return
    if root:
        save_num(tree[root][0])
        cnt += 1
        node[root] = cnt
        save_num(tree[root][1])
 
 
for tc in range(1, T + 1):
    N = int(input())
    # 길이가 짝수면 + 1
    # 아니라면
    num_li = [0] + [i for i in range(1, N + 1)]
    tree = [[0, 0] for _ in range(N + 1)]
    par = [0] * (N + 1)
    node = [0] * (N + 1)
    cnt = 0
    make_tree(1, N)
    save_num(1)
    print(f'#{tc}',node[1],node[N // 2])
    print(tree)