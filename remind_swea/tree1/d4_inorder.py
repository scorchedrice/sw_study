def inorder(root):
    global result
    if root != 0:
        inorder(bridge_left[root])
        result += island_name[root]
        inorder(bridge_right[root])
    return
    
for tc in range(1,11):
    island = int(input()) # 정점(노드)의 수
    island_name = ['-'] * (island + 1)
    bridge_left = [0] * (island + 1)
    bridge_right = [0] * (island + 1)

    for i in range(1,island+1):
        info = list(input().split())
        # 우선 받은 정보 중 int로 바꿀 수 있는 것은 미리 바꾸기
        for i in range(len(info)):
            try:
                info[i] = int(info[i])
            except:
                continue
        
        island_name[info[0]] = info[1]
        if len(info) == 3:
            bridge_left[info[0]] = info[2]
        elif len(info) == 4:
            bridge_left[info[0]] = info[2]
            bridge_right[info[0]] = info[3]

    result = ''
    inorder(1)
    print(f"#{tc} {result}")