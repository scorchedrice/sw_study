'''
"가장 적은 비용"으로 수영장 이용 방법
1일 이용권, 1달 이용권, 3달 이용권, 1년 이용권 판매 # 달 이용권은 매달 1일부터 시작
3달 이용권의 경우엔 11월 12월에 이용 및 구매 가능하지만, 11월 12월 1월 처럼 사용하도록 구매 불가하다.
'''
'''
모든 이용권 가격은 10이상 3000이하의 정수
'''
'''
그냥, 1일당 회원권의 가치를 비교해볼까
'''
def DFS(n,lst):
    global min_price
    if n >= 12:
        if sum(lst) < min_price:
            min_price = sum(lst)
        return
    if plan[n+1] != 0:
        DFS(n+1, lst + [plan[n+1]*day_pass])
        DFS(n+1, lst + [M1_pass])
        DFS(n+3, lst + [M3_pass])
    else:
        DFS(n+1, lst)

T = int(input())
for tc in range(1,T+1):
    day_pass, M1_pass, M3_pass, year_pass = map(int,input().split())
    plan = [0] + list(map(int,input().split())) # 1월부터 12월 표기 위함.
    # DFS를 진행한다. 해당 월에 일권을 쓸지 월권을 쓸지 3개월권을 쓸지
    min_price = 987654321
    DFS(0,[])
    if min_price < year_pass:
        print(f"#{tc} {min_price}")
    else:
        print(f"#{tc} {year_pass}")
