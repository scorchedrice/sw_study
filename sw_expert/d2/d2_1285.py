# 돌을 던져 원하는 지점 가까이 가야함
# mm단위로 -100,000 ~ 100,000 까지 숫자가 일렬로 써 있을 때, 100,000에서 0에 가까운 위치로 돌을 던지려고 한다.
# N명의 사람, 0에 가깝게 돌이 떨어진 위치와 0 사이의 거리 차, 몇 명이 그렇게 돌을 던졌는지 주어짐
# 1L ... testcase, 그 다음부터 돌을 던지는 사람 수 N, 그 다음줄 돌이 떨어진 위치 N개 공백으로 구분

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score_list = []
    score_list += list(map(int, input().split()))

    for j in range(len(score_list)):
        score_list[j] = abs(score_list[j])

    score_list.sort()
    score_list.reverse()
    max_score = score_list[0]
    best_player = score_list.count(max_score)
    print(f"#{tc} {max_score} {best_player}")