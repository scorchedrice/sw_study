def enq(n):
    global last
    last += 1
    min_heap[last] = n
    c = last
    p = c//2
    while p>=1 and min_heap[p] > min_heap[c]:
        min_heap[p], min_heap[c] = min_heap[c], min_heap[p]
        c = p
        p = c//2

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    min_heap = [0] * (N+1)
    last = 0
    result = 0
    for i in range(N):
        enq(num_list[i])

    index = N
    while True:
        index = index//2
        result += min_heap[index]
        if index == 0:
            break

    print(f"#{tc} {result}")