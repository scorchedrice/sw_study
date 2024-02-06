최빈수구하기
```python
T = int(input())

N = 1000 #학생의 수

for a in range(0,T):
    t = int(input())
    score_list = list(map(int, input().split()))
    score_list.sort()

    score_group = [score_list[0]]
    score_grouping = []

    for i in range(1,1000):
        if score_list[i] == score_list[i-1]:
            score_group += [score_list[i]]
        elif score_list[i] != score_list[i-1]:
            score_grouping += [score_group]
            score_group = [score_list[i]]
    score_grouping += [score_group]
    
    bin_score = []
    for j in range(0, len(score_grouping)):
        bin_score += [len(score_grouping[j])]
    max_bin = max(bin_score)
    final_dis = []
    for k in range(0, len(bin_score)):
        if max_bin == bin_score[k]:
            final_dis += [score_grouping[k][0]]
    print(f"#{t} {max(final_dis)}")
```
1959. 두개의 숫자열
```python
T = int(input())
#여기서 부터 loop
for i in range(0,T):    
    N, M = list(map(int, input().split()))

    dif_size = abs(N-M)

    if N>M:
        min_size = M
    else:
        min_size = N

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if min_size == M:
        min_list = b
        max_list = a
    else:
        min_list = a
        max_list = b

    cal_list = []
    for j in range(0, dif_size+1):
        cal_num = 0
        for k in range(0,min_size):
            cal_num = cal_num + min_list[k] * max_list[k+j]
        cal_list = cal_list + [cal_num]
    print(f"#{i+1} {max(cal_list)}")
```
