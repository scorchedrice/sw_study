# 8자리 암호
'''
8개의 숫자를 입력 받고
1. 첫 숫자 -= 1 후 맨 뒤로
2. 첫 숫자 -= 2 후 맨 뒤로
3. 첫 숫자 -= 3 후 맨 뒤로 ...

j. 첫 숫자 -= j 후 맨 뒤로
'''
T = 10
for tc in range(1,T+1):
    test_num = int(input())
    pw = list(map(int, input().split()))
    cnt = 0
    minus = 1
    while True:
        pw[cnt] = pw[cnt] - minus
        if pw[cnt] <= 0:
            pw[cnt] = 0
            break
        cnt += 1
        minus += 1
        if cnt == 8:
            cnt = 0
        if minus == 6:
            minus = 1
    # 문제 조건에 따라 빼는 행위를 완료했으니, 0이 마지막에 오도록 재정렬 필요

    notyet_pw = pw + pw
    for k in range(15,-1,-1):
        if notyet_pw[k] == 0:
            print(f"#{tc}", end = ' ') 
            print(*notyet_pw[k-7:k+1])
            break