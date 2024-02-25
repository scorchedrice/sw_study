def my_cal():
    for i in range(N,0,-1):
        if child_list[i] != 0:
            if node[i] == '-':
                node[i] = node[child_list[i][0]] - node[child_list[i][1]]
            elif node[i] == '+':
                node[i] = node[child_list[i][0]] + node[child_list[i][1]]
            elif node[i] == '*':
                node[i] = node[child_list[i][0]] * node[child_list[i][1]]
            elif node[i] == '/':
                node[i] = node[child_list[i][0]] / node[child_list[i][1]]

for tc in range(1,11):
    N = int(input())
    node = [0] * (N+1)
    child_list = [0] * (N+1)
    for i in range(N):
        info = list(input().split())
        len_info = len(info)
        
        # 정수로 바꿀 수 있는 것은 일단 바꾸기
        for k in range(len_info):
            try:
                info[k] = int(info[k])
            except:
                continue
            
        node[info[0]] = info[1]
        if len_info == 3:
            child_list[info[0]] = [info[2]]
        elif len_info == 4:
            child_list[info[0]] = [info[2], info[3]]

    my_cal()
    print(f"#{tc} {int(node[1])}")