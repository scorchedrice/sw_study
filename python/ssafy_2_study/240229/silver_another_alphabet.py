alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
'''
c를 만난 경우 (c=, c-)
d를 만난 경우 (dz=, d-)
l을 만난 경우 (lj)
n을 만난 경우 (nj)
s를 만난 경우 (s=)
z를 만난 경우 (z=)
'''
check_list = input()
len_str = len(check_list)
cnt = 0
index = 0
while True:
    if index >= len_str: # 종료조건
        break
    if check_list[index] == 'c':
        # -, =를 만나면 index 두칸 추가 후 카운트 하나 추가
        if 0<=index+1<=len_str - 1 and check_list[index+1] == '-':
            cnt += 1
            index += 2
            
        elif 0<=index+1<=len_str - 1 and check_list[index+1] == '=':
            cnt += 1
            index += 2
        else:
            cnt += 1
            index += 1
    elif check_list[index] == 'd':
        # z=, -를 만나면 조건에 맞게 index 변화
        if 0<=index+2<=len_str -1 and check_list[index+1] == 'z' and check_list[index+2] == '=':
            cnt += 1
            index += 3
        elif 0<=index+1<=len_str -1 and check_list[index+1] == '-':
            cnt += 1
            index += 2
        else:
            cnt += 1
            index += 1
    elif check_list[index] == 'l':
        # j를 만난 경우의 수 설정
        if 0<=index+1<=len_str -1 and check_list[index+1] == 'j':
            cnt += 1
            index += 2
        else:
            cnt += 1
            index += 1           
    elif check_list[index] == 'n':
        # n을 만난 경우
        if 0<=index+1<=len_str -1 and check_list[index+1] == 'j':
            cnt += 1
            index += 2
        else:
            cnt += 1
            index += 1
    elif check_list[index] == 's':
        # s를 만난 경우
        if 0<=index+1<=len_str -1 and check_list[index+1] == '=':
            cnt += 1
            index += 2
        else:
            cnt += 1
            index += 1
    elif check_list[index] == 'z':
        # z를 만난 경우
        if 0<=index+1<=len_str -1 and check_list[index+1] == '=':
            cnt += 1
            index += 2
        else:
            cnt += 1
            index += 1
    else:
        cnt += 1
        index += 1
print(cnt)