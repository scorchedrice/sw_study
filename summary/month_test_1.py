# Problem1
# max 사용하지 않고 max 함수 정의하기
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 max() 사용 시 감점

def max_score(score_list):
    max_value = score_list[0] # 일단 score_list의 첫째 항을 최대값이라 가정
    for i in range(1,len(score_list)): # 가정한 값과 하나하나 비교하며 max_value를 찾는 과정
        if max_value < score_list[i]:
            max_value = score_list[i]
    return max_value
    
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
scores1 = [30, 60, 90, 70]
print(max_score(scores1)) # 90
#####################################################

# Problem2
# 시험 점수 관리 코드 작성, 60점 이상 과목 개수 계산
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def over(score_list): 
    count = 0 # 총 몇번이나 60점을 넘는지 세기 위한 준비
    for i in score_list:
        if i >= 60:
            count += 1 # 넘는 것이 하나 있을 때 마다 count + 1
    return count
    # 여기에 코드를 작성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
scores1 = [30, 60, 90, 70]
print(over(scores1)) # 3
#####################################################

# Problem3
# 인자로 음식 dict.를 받고 이를 활용하여 판매 메뉴 개수를 반환하는 함수 정의
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count() 를 사용시 감점
def menu_count(restorant_dict):
    menu_list = restorant_dict["menus"]
    return len(menu_list)
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
restorant1 = {
    "id": 11,
    "user_rating": 5.5,
    "name": "김밥나라",
    "menus": ["참치김밥", "치즈라면", "돈까스", "비빔밥"],
    "location": "서울특별시 강남구 역삼동 123-123"
}
print(menu_count(restorant1)) # 4
#####################################################

# Problem3 - len 사용X
# 인자로 음식 dict.를 받고 이를 활용하여 판매 메뉴 개수를 반환하는 함수 정의
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count() 를 사용시 감점
def menu_count(restorant_dict):
    menu_list = restorant_dict["menus"]
    len = 0
    for list in menu_list:
        len += 1
    return len

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
restorant1 = {
    "id": 11,
    "user_rating": 5.5,
    "name": "김밥나라",
    "menus": ["참치김밥", "치즈라면", "돈까스", "비빔밥"],
    "location": "서울특별시 강남구 역삼동 123-123"
}
print(menu_count(restorant1)) # 4
#####################################################

# Problem4
# 2차원 list [최고온도, 최저온도]
# dict을 구성한다. (key - minumum, maximum | value는 list형식)
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def turn(temperature_list):
    new_list = {}
    max_list = []
    min_list = []
    for day in range(0,len(temperature_list)):
        max_list += [temperature_list[day][0]]
        min_list += [temperature_list[day][1]]
    new_list["maximum"] = max_list
    new_list["minumum"] = min_list
        
    return new_list
    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
temperatures1 = [
    [9, 3],
    [9, 0],
    [11, -3],
    [11, 1],
    [8, -3],
    [7, -3],
    [-4, -12]
]
print(turn(temperatures1)) 
# {'maximum': [9, 9, 11, 11, 8, 7, -4], 'minimum': [3, 0, -3, 1, -3, -3, -12]}
#####################################################

# Problem5
# ID, PW 빈 값 입력 방지, 입력 ID/PW 중 하나라도 공백이 있다면 False, 아니면 True 출력
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user):
    id = user['id']
    pw = user['password']
    check = id+pw # id와 pw를 이어 붙힌 str 생성
    if check == pw or check == id: # 빈 칸이 입력된 경우 이어 붙힌 값이 id 혹은 pw와 일치하므로
        return False
    else:
        return True


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 

user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################

# Problem6
# id 마지막 문자열 0~9 사이숫자
# 위 조건 만족시 True 아니면 False
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user):
    check_id = user['id'][-1]
    if check_id.isdecimal() == 1:
        return True
    else:
        return False   
    
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True

user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################