'''
N개의 정수와 M개의 정수가 주어진다.
N개의 정수가 주어지면 정렬 후 A에 저장한다.
이후 주어지는 M개의 정수를 이진탐색으로 탐색한다
(A의 수가 들어 있는지)
탐색 과정에서 번갈아 가며 선택하는 경우엔 이를 도출하고
아니면 pass
'''
def bin(target, N):
    global dir
    start = 0
    end = N-1
    dir = 0
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            return 1
        
        if A[mid] > target: # 기준이 더 큰 경우 (왼쪽탐색 필요)
            end = mid -1
            if dir == 'L':
                return 0
            else:
                dir = 'L'
    
        elif A[mid] < target: # 기준이 더 작은 경우 (우측탐색 필요)
            start = mid + 1
            if dir == 'R':
                return 0
            else:
                dir = 'R'
    return 0


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = list(map(int,input().split()))
    dir = 0
    total = 0
    for i in range(M):
        total += bin(B[i], N)
    print(f"#{tc} {total}")