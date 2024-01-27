# 왕실의 나이트
# 나이트 이동 : 종2횡1, 횡2종1
# 나이트의 위치를 입력받으면 이동 가능한 경우의 수를 출력

knight_position = input() # 좌표 입력
knight_position = [knight_position[0], int(knight_position[1])] # 입력된 좌표 앞글자(행), 뒷글자(열)

def change_coord(knight_position): # 입력받은 좌표 앞부분(영어)를 숫자로 전환하는 함수
    x = ['a','b','c','d','e','f','g','h']
    coord_num = 1
    for alpha in x:
        if knight_position[0] == alpha:
            knight_position[0] = coord_num
        else:
            coord_num += 1
    return knight_position

change_coord(knight_position)

def cal_case(knight_position): # 경우의 수를 계산하는 함수 정의
    count = 0
    
    def garo(knight_position): # 종2횡1 이동 가능한 경우의 수
        x = knight_position[1]
        y = knight_position[0]
        count = 0
        if 1<= x+2 <=8 and 1<= y+1 <=8:
            count += 1
        
        if 1<= x+2 <=8 and 1<= y-1 <=8:
            count += 1

        if 1<= x-2 <=8 and 1<= y+1 <=8:
            count += 1
        
        if 1<= x-2 <=8 and 1<= y-1 <=8:
            count += 1
        
        return count

    count = count + garo(knight_position)

    def saero(knight_position): #횡2종1 이동 가능한 경우의 수
        x = knight_position[1]
        y = knight_position[0]
        count = 0
        if 1<= x+1 <=8 and 1<= y+2 <=8:
            count += 1
        
        if 1<= x+1 <=8 and 1<= y-2 <=8:
            count += 1

        if 1<= x-1 <=8 and 1<= y+2 <=8:
            count += 1
        
        if 1<= x-1 <=8 and 1<= y-2 <=8:
            count += 1
        
        return count
    
    count = count + saero(knight_position)

    return count

print(cal_case(knight_position))