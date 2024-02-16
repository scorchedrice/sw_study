maze = []
for k in range(16):
    maze += [list(map(int, input()))]
def test():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j

r1, r2 = test()
print(r1, r2)

