def preorder(root):
    global cnt
    if left[root] != 0:
        cnt += 1
        preorder(left[root])
    else:
        return
    if right[root] != 0:
        cnt += 1
        preorder(right[root])
    else:
        return
    
T = int(input())
for tc in range(1,T+1):
    bridge, subtree_root = map(int,input().split())
    info = list(map(int,input().split()))
    left = [0] * (bridge + 2) # index를 번호로 가지는 노드의 자식이 무엇인지
    right = [0] * (bridge + 2)

    for i in range(0,len(info),2):
        a, b = info[i], info[i+1]
        if left[a] == 0:
            left[a] = b
        else:
            right[a] = b

    cnt = 1
    preorder(subtree_root)
    print(f"#{tc} {cnt}")