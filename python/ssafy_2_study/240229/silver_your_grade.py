# 너의 평점은 ..?
'''
학점은 1.0 2.0 3.0 4.0 중 하나
점수는 A+ 4.5, A0 4.0, B+ 3.5, B0 3.0, C+ 2.5, C0 2.0, D+ 1.5, D0 1.0, F 0.0
         0      1       2       3       4       5        6      7       8
'''

grade_num = 0
for_div = 0 # 학점 계산
# A+ ~ F까지 몇개나 있나 카운트 하기 위함
for _ in range(20):
    info = input()
    if info[-1] == 'P':
        continue
    elif info[-1] == 'F':
        for_div += float(info[-5:-2])
    elif info[-1] == '+':
        if info[-2] == 'A':
            grade_num += 4.5*float(info[-6:-2])
            for_div += float(info[-6:-2])
        elif info[-2] == 'B':
            grade_num += 3.5*float(info[-6:-2])
            for_div += float(info[-6:-2])
        elif info[-2] == 'C':
            grade_num += 2.5*float(info[-6:-2])
            for_div += float(info[-6:-2])
        elif info[-2] == 'D':
            grade_num += 1.5*float(info[-6:-2])
            for_div += float(info[-6:-2])
    elif info[-1] == '0':
        if info[-2] == 'A':
            grade_num += 4.0*float(info[-6:-2])
            for_div += float(info[-6:-2])
        elif info[-2] == 'B':
            grade_num += 3.0*float(info[-6:-2])
            for_div += float(info[-6:-2])
        elif info[-2] == 'C':
            grade_num += 2.0*float(info[-6:-2])
            for_div += float(info[-6:-2])
        elif info[-2] == 'D':
            grade_num += 1.0*float(info[-6:-2])
            for_div += float(info[-6:-2])
print(grade_num/for_div)