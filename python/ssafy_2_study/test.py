# 합이 t인 부분집합 찾기
# Example3.
def f(i,k,s,t):
    if s == t:
        for j in range(k):
            if bit[j]:
                print(A[j], end = ' ')
        print()
    elif i == k: # 모든 원소를 고려했으나, 값에 도달하지 못한경우
        return
    elif s>t:
        return
    else: # 결정이 끝나지 않았다면
        bit[i] = 1
        f(i+1,k,s+A[i],t)
        bit[i] = 0
        f(i+1,k,s,t)

N = 10 # 원소의 개수
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0]*N # bit[i]는 A[i]가 부분집합에 포함되냐를 의미함
f(0,N,0,10)