total = [0] * 31
total[1] = 1
total[2] = 3
for k in range(3,31):
    total[k] = total[k-1] + 2*total[k-2]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f"#{tc} {total[N//10]}")
