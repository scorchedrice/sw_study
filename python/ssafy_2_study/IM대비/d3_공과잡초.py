def change(field_lst):
    len_field = len(field_lst)
    cnt = 0
    for i in range(len_field - 1):
        if field_lst[i] == '(' and field_lst[i+1] == '|':
            cnt += 1
        if field_lst[i] == '(' and field_lst[i+1] == ')':
            cnt += 1
        if field_lst[i] == '|' and field_lst[i+1]  == ')':
            cnt += 1
    return cnt

T = int(input())
for tc in range(1,T+1):
    field = list(input())
    print(f"#{tc} {change(field)}")