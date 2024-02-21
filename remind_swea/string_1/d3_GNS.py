'''
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
0      1     2       3        4      5     6        7     8      9
'''
another_language = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1,T+1):
    testcase, N = input().split()
    N = int(N)
    print(testcase)
    need_to_trans = list(input().split())
    for k in another_language:
        for l in range(N):
            if k == need_to_trans[l]:
                print(k, end= ' ')
    print()