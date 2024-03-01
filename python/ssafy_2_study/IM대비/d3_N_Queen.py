def dfs(n,lst):
    global candidate
    if n == N:
        candidate += 1
        return
    for i in range(N):
        if visited[i] == 0 and lst == []:
            visited[i] = 1
            dfs(n+1, lst + [i])
            visited[i] = 0
        elif visited[i] == 0 and lst != []:
            can_i_continue = True
            for k in range(len(lst)):
                if abs(len(lst) - k) == abs(i - lst[k]):
                    # 재귀 진행하기 전에 수시로 체크
                    can_i_continue = False
                    break
            if can_i_continue == True:
                visited[i] = 1
                dfs(n+1, lst + [i])
                visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    candidate = 0
    visited = [0] * (N)
    dfs(0,[])
    print(f"#{tc} {candidate}")