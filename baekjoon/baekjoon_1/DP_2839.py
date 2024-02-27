'''
N 킬로그램을 배달해야 한다.
설탕은 봉지에 담겨져 있으며, 3킬로그램 봉지와 5킬로그램 봉지가 있다.
최대한 적은 봉지를 들고가려 한다.
'''
N = int(input())
# 5a + 3b = N을 만족하면서, (a+b)가 최소임을 판단하는 함수 제작
# 가장 많이 봉지를 들고가는 경우는 3킬로 봉지만을 들고가는 경우이므로 이를 정지조건으로

max_bag = N//3

def dfs(n,lst):
    global ans
    if n == 2:
        if 3*lst[0] + 5*lst[1] == N:
            if ans > sum(lst):
                ans = sum(lst)
        return
    for i in range(N//3+1):
        dfs(n+1, lst+[i])
    
ans = 987654321
dfs(0,[])
if ans == 987654321:
    print('-1')
else:
    print(ans)