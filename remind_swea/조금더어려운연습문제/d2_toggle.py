'''
Toggle : 0은 1로, 1은 0으로 바꾸는 연산
M초까지 초당 1회 조건부 토글 진행, 조건은 아래와 같다.
1) i,j는 1부터 시작하고 N이 마지막이다. (index주의)
2) k초가 될 때
    만약 i+j == k * n (n은 자연수)라면 i+j가 그 조건을 만족하는 영역은 토글된다.
        단! M이 k의 배수인 경우와 M초인 경우, 이를 무시하고 전체가 토글된다.
'''

# 문제풀이 전략
'''
1) 조건을 만족할 때 (+ 예외조건을 충족하지 않고) 토글연산하는 함수
2) 예외조건을 충족할 때, 전체를 토글연산하는 함수
3) 최종 결과로 1의 개수를 세는 함수
위 세가지 함수를 정의한다.

더불어 인덱스 오류가 발생할 수 있으니, 이를 방지하기 위해 0의 인덱스를 추가한다.
0과 1이 바뀌는 연산이므로 이와 상관없는 9를 0인덱스가 포함된 matrix 영역에 할당한다.
'''
def all_toggle():
    for i in range(1,N+1):
        for j in range(1,N+1):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            elif matrix[i][j] == 0:
                matrix[i][j] = 1 
    

def normal_toggle(k):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if (i+j)%k == 0:
                if matrix[i][j] == 1:
                    matrix[i][j] = 0
                elif matrix[i][j] == 0:
                    matrix[i][j] = 1
    
def count_one():
    cnt = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if matrix[i][j] == 1:
                cnt += 1
    return cnt
# T = int(input())
# for tc in range(1,T+1):
N, M = map(int,input().split())
# N은 matrix의 사이즈, M은 몇초동안 토글

# matrix 0행부분을 9로 만들고 시작
matrix = [[9 for _ in range(N+1)]]
for _ in range(N):
    matrix += [[9] + list(map(int,input().split()))]
    # 행을 추가할 때, 0열 부분을 9라고 하고 추가

for k in range(1,M+1):
    # 1초부터 M초까지 고려한다.
    if M%k == 0: # M이 k의 배수인 경우
        all_toggle() # 모두 토글

    else: # 그 외의 경우
        normal_toggle(k) # i+j가 k의 배수인 영역만 토글

print(count_one())
    
