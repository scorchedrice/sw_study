'''
0초에서 시작하여 100초간 두 전구가 언제 켜지는지 관찰
전구 X는 시작 경과 후 A초에서부터 관찰시작 경과 후 B초까지에만 켜져 있었다.
전구 Y는 관찰 시작 경과 후 C초에서부터 관찰 시작 경과 후 D초까지에만 켜져 있었다.

X ... A~B
Y ... C~D
100초 중 두 전구가 동시에 켜져있던 시간은?
'''

T = int(input())
result = []
for tc in range(1,T+1):
    A,B,C,D = map(int,input().split())
    # A가 B보다 작고, C가 D보다 작은 것은 보장되어 있다.
    start = max(A,C)
    end = min(B,D)
    if start > end:
        result.append(0)
    else:
        result.append(end-start)
for tc in range(1,T+1):
    print(f"#{tc} {result[tc-1]}")