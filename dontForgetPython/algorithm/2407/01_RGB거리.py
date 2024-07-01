N = int(input())
matrix = []
dp = []
for _ in range(N):
    layer = list(map(int,input().split()))
    matrix.append(layer)
    if _ == 0:
        dp.append(layer)
    else:
        dp_layer = []
        for choose in range(3):
            if choose == 0:
                dp_layer.append(layer[0]+min(dp[-1][2], dp[-1][1]))
            elif choose == 1:
                dp_layer.append(layer[1]+min(dp[-1][0], dp[-1][2]))
            else:
                dp_layer.append(layer[2]+min(dp[-1][0], dp[-1][1]))
        dp.append(dp_layer)
print(min(dp[-1]))
