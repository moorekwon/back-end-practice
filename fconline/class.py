# python class
# self, class, instance 변수

# class와 instance의 차이
# namespace: 객체를 인스턴스화 할 때 저장된 공간
# class 변수: 직접 사용 가능, 객체보다 먼저 생성
# instance 변수: 객체마다 별도로 존재, 인스턴스 생성 후 사용

class UserInfo:
    def __init__(self, name):
        self.name = name
        
    def print_info(self):
        print('print_info > ', self.name)
        
    # def __del__(self):
    #     print('instance removed!')
        
user1 = UserInfo('Kwon')
print(id(user1))
print(user1.__dict__)
print(user1.name)

user2 = UserInfo('Park')
print(id(user2))
print(user2.__dict__)
print(user2.name)