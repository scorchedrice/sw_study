# 주어진 정수의 범위 1 이상 10^18 이하
# 즉 X의 범위는 1이상 10^6 이하

def check_triple(N):
    start = 0
    end = 1000000
    while start<=end:
        mid = (start+end)//2
        if triple_list[mid] == N:
            return mid
        elif triple_list[mid] < N:
            start = mid + 1
        else:
            end = mid - 1
    return -1

T = int(input())

triple_list = [num**3 for num in range(1000001)]

for tc in range(1,T+1):
    N = int(input())
    print(f"#{tc} {check_triple(N)}")    
