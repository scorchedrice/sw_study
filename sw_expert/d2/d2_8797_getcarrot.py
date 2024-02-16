'''
각 구역별로 탐색하는 알고리즘을 작성한다. (1,2,3,4)
이후 이 함수를 각각 적용시키고 최대값과 최소값을 구한 후 결론을 도출한다.
'''
'''
Sector1 
0행 1열부터 N-2열까지
1행 2열부터 N-3열까지
...
N//2-1 행 N//2열부터 N//2열까지

Sector4
1행 0열부터 0열까지
2행 0열부터 1열까지
...
N//2-1 행 0열부터 N//2 -2열까지
N//2행 0열부터 N//2 -1열까지 (탐색구간 제일 김)
N//2+1 행 0열부터 N//2 -2열까지
...
N-3 행 0열부터 1열까지
N-2 행 0열부터 0열까지
'''
def count_sector1():
    result = 0
    for i in range(N//2):
        result += sum(map_info[i][i+1:N-i])
    return result

def count_sector2():
    result = 0
    for i in range(1,(N//2)+1):
        result += sum(map_info[i][N-i:N])
    for k in range(N-2, N//2, -1):
        result += sum(map_info[k][k+1:N])
    return result

def count_sector3(num1, num2, num4):
    total = 0
    for i in range(N):
        total += sum(map_info[i])
    return total - (num1 + num2 + num4)
    
def count_sector4():
    result = 0
    for i in range(1,(N//2)+1):
        result += sum(map_info[i][0:i])
    for k in range(N-2, N//2, -1):
        result += sum(map_info[k][0:N-1-k])
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    map_info = [list(map(int, input().split())) for _ in range(N)]

    num1 = count_sector1()
    num2 = count_sector2()
    num4 = count_sector4()
    num3 = count_sector3(num1,num2,num4)
    max_value = max([num1,num2,num3,num4])
    min_value = min([num1,num2,num3,num4])
    print(f"#{tc} {max_value - min_value}")