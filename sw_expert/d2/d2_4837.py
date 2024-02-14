'''
def my_nCr(input_list, r):
    result = []
    if r == 0:
        return [[]]
    
    for _ in range(0,len(input_list)):
        element = input_list[_]
        rest_element = input_list[_ + 1 :]
        for C in my_nCr(rest_element, r-1):
            result += [[element] + C]
    return result

def find_K(result):
    real_result = []
    for _ in result:
        if sum(_) == K:
            real_result += [_]
    return real_result

A = list(range(1,13))
T = int(input())
for tc in range(1,T+1):
    r, K = map(int, input().split())
    print(f"#{tc} {len(find_K(my_nCr(A,r)))}")
    '''

T = int(input())
pivot = list(range(1,13))
for tc in range(1,T+1):
    n,k = map(int, input().split())
    bit = [0]*12
    ans = 0
    result = []
    for i in range(1<<12): # 1<<n : 부분 집합의 개수
        semi_result = []
        for j in range(12): # 원소의 수만큼 비트를 비교
            if i&(1<<j): # i의 j번째 비트가 1인 경우 (0또는 0이 아님(1))
                semi_result += [pivot[j]]
        if sum(semi_result) == k and len(semi_result) == n:
            result += [semi_result]
    print(f"#{tc} {len(result)}")