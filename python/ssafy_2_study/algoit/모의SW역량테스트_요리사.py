def dfs(n,lst,size, arr_len):
        if n == size:
            a_material.append(lst)
            memory = []
            for j in range(arr_len):
                 if visited[j] == 0:
                      memory.append(j)
            b_material.append(memory)
            return

        for i in range(arr_len):
            if visited[i] == 0 and lst== []:
                visited[i] = 1
                dfs(n+1,lst+[i],size,arr_len)
                visited[i] = 0
            elif visited[i] == 0 and lst != []:
                if lst[-1] < i:
                    visited[i] = 1
                    dfs(n+1,lst+[i],size,arr_len)
                    visited[i] = 0
    
def cal_score(n, lst, arr_a, arr_b, arr_len):
    global a_score
    global b_score
    if n == 2:
        x = lst[0]
        y = lst[1]
        a = arr_a[x]
        b = arr_a[y]
        c = arr_b[x]
        d = arr_b[y]
        a_score += table[a][b] + table[b][a]
        b_score += table[c][d] + table[d][c]
        return
    
    for i in range(arr_len):
        if visited[i] == 0 and lst == []:
            visited[i] = 1
            cal_score(n+1,lst+[i],arr_a,arr_b,arr_len)
            visited[i] = 0
        elif visited[i] == 0 and lst != []:
            if lst[-1] < i:
                    visited[i] = 1
                    cal_score(n+1,lst+[i],arr_a, arr_b,arr_len)
                    visited[i] = 0
         
         
T = int(input())
for tc in range(1,T+1):
    table = []
    N = int(input())
    for _ in range(N):
        table.append(list(map(int,input().split())))
    a_material = []
    b_material = []
    visited = [0] * N
    dfs(0,[],N//2,N)
    material_candidate = len(a_material)
    len_arr = len(a_material[0])
    min_score = 987654321
    a_score = 0
    b_score = 0
    for k in range(material_candidate):
        visited = [0] * len_arr
        cal_score(0,[],a_material[k],b_material[k],len_arr)
        if min_score > abs(a_score - b_score):
            min_score = abs(a_score - b_score)
        a_score = 0
        b_score = 0
    print(f"#{tc} {min_score}")