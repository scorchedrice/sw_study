for tc in range(1,11):
    N, password = input().split()
    N = int(N)
    password = list(password)

    while True:
        cnt_change = 0
        len_pw = len(password)
        for k in range(len_pw-1):
            if password[k] == password[k+1]:
                del password[k]
                del password[k]
                cnt_change += 1
                break
        if cnt_change == 0:
            break
    print(f"#{tc}", end= ' ')
    for k in password:
        print(k, end = '')
    print()