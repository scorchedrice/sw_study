def postorder(root):
    if root > island:
        return 0
    if island_name[root] != 0:
        # leaf에 도달하면
        return island_name[root]
    left = postorder(2*root)
    right = postorder(2*root+1)
    island_name[root] = left + right
    return island_name[root]

T = int(input())
for tc in range(1,T+1):
    island, leaf, target = map(int,input().split())
    island_name = [0] * (island + 1)
    for _ in range(leaf):
        a, b = map(int,input().split())
        island_name[a] = b

    postorder(1)
    print(f"#{tc} {island_name[target]}")