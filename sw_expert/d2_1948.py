# 날짜계산 - 누적 리스트 생성 및 항목 추가
month_info = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count = 0
days_info = [0]
for days in month_info:
    count = count + days
    days_info.append(count)

t = int(input())
for i in range(1,t+1):
    date_list = list(map(int, input().split()))
    # 몇월 몇일 몇월 몇일

    front_day = days_info[date_list[0]-1] + date_list[1]
    back_day = days_info[date_list[2]-1] + date_list[3]
    print(f"#{i} {back_day - front_day + 1}")
