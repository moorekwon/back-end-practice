# python 흐름제어(제어문)
# 조건문

# print(type(True))
# print(type(False))

# 기본 형식

# if True:
#     print('Yes')
# if False:
#     print('No')
    
# if False:
#     print("You can't reach here.")
# else:
#     print("Oh, you are here.")

# 관계 연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

# print(a != b)
# print(a > b)

# 참, 거짓 종류
# 참: "~", [~], (~), {~}, 1
# 거짓: "", [], (), {}, 0, None

# city = "seoul"

# if city:
#     print('You aere in: ', city)
# else:
#     print('Please enter your city.')

# 논리 연산자
# and, or, not

a = 100
b = 60
c = 15

# print(a > b and b > c)
# print(a > b or b > c)
# print(not a > b)
# print(not b > c)
# print(not True)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서

# print(3 + 12 > 7 + 3)
# print(5 + 10 * 3 > 7 + 3 * 20)
# print(5 + 10 > 3 and 7 + 3 == 10)
# print(5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

# if score1 >= 90 and score2 == 'A':
#     print("합격하셨습니다.")
# else:
#     print('불합격입니다.')

id1 = 'gold'
id2 = 'admin'
id3 = 'super'

# if id1 == 'gold' or id2 == 'admin':
#     print("관리자 로그인 성공")

# if id2 == 'admin' and id3 == 'super':
#     print('최고 관리자 로그인 성공')

is_work = False

if is_work:
    print('is work!')
    
# 다중 조건문
num = 90

# if num >= 70:
#     print(num)
# elif num >= 60:
#     print(num)
# else:
#     print('default num')
    
# 중첩 조건문
age = 27
height = 175

# if age >= 20:
#     if height >= 170:
#         print('A지망 지원 가능')
#     elif height >= 160:
#         print('B지망 지원 가능')
#     else:
#         print('지원 불가')
# else:
#     print('20세 이상 지원 가능')

# in, not in
q = [1, 2, 3]
w = {7, 8, 9, 9}
e = {'name': 'Kwon', 'city': 'seoul', 'grade': 'B'}
r = (10, 12, 14)

print(1 in q)
print(6 in w)
print(12 not in r)
print('name' in e)
print('seoul' in e.values())