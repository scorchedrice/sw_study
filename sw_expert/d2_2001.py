#파리퇴치
t = int(input())
N, M = list(map(int, input().split()))
total_map = []
for i in range(0, N):
    total_map.append(list(map(int, input().split())))

hit_range = N-M+1
sum_fly = 0
for j in range(0,hit_range):
    for k in range(0,hit_range):
        sum_fly = sum_fly + total_map[j][k]

print(sum_fly)

