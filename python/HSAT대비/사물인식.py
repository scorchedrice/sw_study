'''
인식된 정보의 입력값 : 평면에 N개의 점으로 주어짐
각각의 점들은 K개의 색 중 하나(1,2,...,K)

입력값으로 주어진 K개의 색에 대해 해당 색을 가지는 점들을 적어도 하나씩포함하는 사물 중
넓이가 가장 "작은 것"을 찾고 그 넓이를 출력하는 프로그램 작성
    - 직사각형으로 인식되어야한다.
가로 또는 세로의 길이가 0이되어 넓이가 0이 되는 경우도 존재한다. (하나의 좌표에 여러개의 점 가능)
'''
'''
문제풀이 흐름
1. K개의 색상을 하나 씩 선택한 list 생성한다.
2. K개의 색상 들을 하나 씩 선택한 목록에서 x의 최대/최소, y의 최대/최소를 선택하고 계산한다.
    2.1 이 과정을 통해 최소 넓이를 구한다.
'''
def dfs(n,lst_x,lst_y):
    global mn
    if mn == 0: # 최소가 0인 경우 그 아래로 내려가는 경우가 없으니, 이후 연산은 불필요
        return    
    if lst_x != [] and lst_y != []: # 백트래킹을 진행하면서 넓이를 계산해 불필요한 연산을 방지한다.
        xs = min(lst_x) # x_lst, y_lst로 구성하는게 아닌, xe, xs, ys, ye를 가지고 백트래킹을 진행했다면
        xe = max(lst_x) # 이와 같은 연산을 줄일 수 있었을 듯 - 까비
        ys = min(lst_y)
        ye = max(lst_y)
        if abs(xe-xs)*abs(ye-ys) >= mn:
            return
    if n == K+1:
        if mn > abs(xe-xs)*abs(ye-ys): # K개의 색상을 다 고른경우엔
            mn = abs(xe-xs)*abs(ye-ys) # mn값을 갱신한다.
        return
    for k in range(len(color[n])):
        x = color[n][k][0]
        y = color[n][k][1]
        dfs(n+1,lst_x+[x],lst_y+[y])

N, K = map(int,input().split())

color = [[] for _ in range(K+1)]
for _ in range(N):
    x,y,k = map(int,input().split())
    color[k].append([x,y]) # k의 색상인 좌표 입력
mn = 4000000 # 좌표가 -1000 ~ 1000 이므로 가장 큰 값은 2000 * 2000
dfs(1,[],[])
print(mn)