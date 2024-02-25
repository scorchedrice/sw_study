# 이진탐색 - 본인 힘으로
def inorder(root):
    global num
    if root <= N:
        inorder(2*root)
        paper[root] = num
        num += 1
        inorder(2*root+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = 1
    paper = [0] * (N+1)
    inorder(1)
    print(f"#{tc} {paper[1]} {paper[N//2]}")
