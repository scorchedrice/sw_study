'''
가로선 혹은 세로선을 그어 4개의 영역으로 나누고 각 영역 합 중 최대값과 최소값의 차를 구하는 문제
각 영역은 한개이상의 원소가 보장되어야하고, 각 배열의 칸에는 100이하의 자연수가 들어있다.
'''

# 우선 영역을 나눈다.
'''
2차원 평면의 사분면 이름으로 설명하자면
1. 1사분면 : 0행부터 i행 "전"까지, j열부터 마지막열까지
2. 2사분면 : 0행부터 i행 "전"까지, 0열부터 j열 "전"까지
3. 3사분면 : i행부터 마지막행까지, 0열부터 j열 "전"까지
4. 4사분면 : i행부터 마지막행까지, j열부터 마지막열까지
- i는 1이상, 마지막행이하(N-1까지)의 값을 가지고
- j는 1이상, 마지막열이하(N-1까지)의 값을 가진다.
'''
def sector1(i,j):
    result = 0
    for m in range(0,i):
        for n in range(j,N):
            result += matrix[m][n]
    return result

def sector2(i,j):
    result = 0
    for m in range(0,i):
        for n in range(0,j):
            result += matrix[m][n]
    return result

def sector3(i,j):
    result = 0
    for m in range(i,N):
        for n in range(0,j):
            result += matrix[m][n]
    return result

def sector4(i,j):
    result = 0
    for m in range(i,N):
        for n in range(j,N):
            result += matrix[m][n]
    return result

def max_min_sector():
    result = [sector1(i,j),sector2(i,j),sector3(i,j),sector4(i,j)]
    return max(result) - min(result)

# T = int(input())

# 사이즈를 입력받고, 값을 입력받아 매트릭스를 구성한다.
N = int(input())
matrix = []
for _ in range(N):
    matrix += [list(map(int,input().split()))]

result = []
for i in range(1,N):
    for j in range(1,N):
        result += [max_min_sector()]
print(result)