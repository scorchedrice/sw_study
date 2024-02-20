# 회문이면 1 출력, 아니면 0 출력
T = int(input())
for tc in range(1,T+1):
    check_str = input()
    a = 0
    b = len(check_str) -1
    this_is_palindrome = True
    while True:
        # a + b = len(check_str)-1
        # b = len(check_str)-1-a
        if check_str[a] != check_str[b]:
            this_is_palindrome = False
            break
        a += 1
        b -= 1
        
        if b<a:
            break
    
    if this_is_palindrome == True:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")