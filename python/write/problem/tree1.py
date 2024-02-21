'''
주어진 이진트리에서 노드 N을 루트로 하는 서브트리에 속한 노드의 개수를 알아낼 것
주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고
부모가 없는 노드가 전체의 루트 노드가 된다.
'''
def find_parent(parent):
    cnt = 0
    if left[parent] != 0:
        cnt += 1
        cnt += find_parent(left[parent])
    if right[parent] != 0:    
        cnt += 1
        cnt += find_parent(right[parent])
    return cnt

T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split())
    # E는 부모 자식 노드의 쌍 개수

    left = [0] * (E+2)
    right = [0] * (E+2)
    info_list = list(map(int,input().split()))

    for k in range(0,len(info_list),2):
        par, son = info_list[k], info_list[k+1]
        if left[par] == 0:
            left[par] = son
        else:
            right[par] = son
    result = []
    print(f"#{tc} {find_parent(N)+1}")