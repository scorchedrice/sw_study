def find_pw(input_str):
    stack = [input_str[0]]
    for i in range(1, len(input_str)):
        if stack == []:
            stack += [input_str[i]]
        
        elif stack[-1] == input_str[i]:
            stack.pop()
        
        else:
            stack += input_str[i]
    
    return stack

for tc in range(1,11):
    N, input_str = input().split()
    print_list = find_pw(input_str)
    print(f"#{tc}", end = ' ')
    for i in range(len(print_list)):
        print(print_list[i], end = '')
    print()
