T = int(input())
for tc in range(1,T+1):
    A, B = input().split()
    result = ''
    my_index = 0
    count = 0
    while result != A:
        if my_index == len(A):
            break
        if my_index <= (len(A) - len(B)):
            if A[my_index:my_index+len(B)] == B:
                result += B
                my_index += len(B)
                count += 1
            else:
                my_index += 1
                count += 1
        else:
            my_index += 1
            count += 1

    print(f"#{tc} {count}")