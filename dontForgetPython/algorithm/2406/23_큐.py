from collections import deque
import sys

q=deque()
n=int(input())
for _ in range(n):
    qq=sys.stdin.readline().rstrip('\n')
    if qq == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else: print('-1')

    elif qq == 'size': print(len(q))

    elif qq == 'empty':
        if len(q) == 0: print('1')
        else: print('0')

    elif qq == 'front':
        if len(q) != 0: print(q[0])
        else: print('-1')

    elif qq == 'back':
        if len(q) != 0: print(q[len(q)-1])
        else: print('-1')

    else: q.append(qq[5:])
