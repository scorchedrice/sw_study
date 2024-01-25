# 시각
# int N 입력, 00시 00분 00초 ~ N시 59분 59초까지 범위에서 3이 하나라도 포함되는 경우 수 세기
# 풀이 설계 : 분은 59분까지고 초는 59초까지 표시됨 이 범위내에 3이 몇개 있는지 확인하고 loop
# 또 시간이 주어지면 그만큼 그 행위를 반복하면 된다는 것이니 이를 반복
N = int(input()) # N 입력

def cal_time(N):
    num_list_1 = list(range(0,6))
    num_list_2 = list(range(0,10))
    num_total = []
    for min_1 in num_list_1:
        for min_2 in num_list_2:
            for sec_1 in num_list_1:
                for sec_2 in num_list_2:
                    num_total = num_total + [[min_1, min_2, sec_1, sec_2]]
                    # [0,0,0,0] ~ [5,9,5,9] 로 00분 00초부터 59분 59초 까지 리스트화
    
    default = 0
    for i in range(0,len(num_total)):
        if 3 in num_total[i]: # 리스트 중에 3이 존재한다면 1을 더해서
            default = default + 1 # 3이 있는 것이 몇개인지 구하고
    
    ans = 0
    for i in range(0,N+1): # N이 주어졌을때, 0시, 1시 ... 순서대로 계산을 하되
        if i == 3 or i == 13 or i == 23: # 3이 들어있는 시간인 경우는 3600을 더한다.
            ans = ans + 3600
        else: # 그 외의 상황에는 전에 구한 default값을 더하는 과정을 반복한다.
            ans = ans + default
    return ans

print(cal_time(N))
