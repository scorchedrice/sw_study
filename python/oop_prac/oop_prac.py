'''
class Person:
    # 속성
    blood_color = 'red'

    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name} 가 노래합니다.'
    
# 이 과정을 통해 인스턴스 생성
singer1 = Person('iu')
singer2 = Person('bts')
#매서드 호출
print(singer1.singing())
print(singer2.singing())

#속성 접근
print(singer1.blood_color)
'''
'''
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()

p2 = Person()
p2.name = 'Kim'
p2.talk()

print(Person.name)
'''
'''
class Samplecal:
    def add(self, score1, score2):
        self.score1 = score1
        self.score2 = score2
        return self.score1 + self.score2

cal_1 = Samplecal() # 인스턴스를 만들어줘!, 그 인스턴스 이름을 cal_1이라고 할게
#Samplecal.add(cal_1,0,3)
print(cal_1.add(0,3))
'''
class Account:
    account_num = 0

    def __init__(self, name):
        self.name = name
        Account.account_num += 1
    
    def prt_account(self):
        print(f"{self.name}, {Account.account_num}")

p1 = Account("나")
p1.prt_account()
p2 = Account("너")
p2.prt_account()