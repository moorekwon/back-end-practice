# # python 흐름제어(제어문)
# # 조건문

# # print(type(True))
# # print(type(False))

# # 기본 형식

# # if True:
# #     print('Yes')
# # if False:
# #     print('No')
    
# # if False:
# #     print("You can't reach here.")
# # else:
# #     print("Oh, you are here.")

# # 관계 연산자
# # >, >=, <, <=, ==, !=

# a = 10
# b = 0

# # print(a != b)
# # print(a > b)

# # 참, 거짓 종류
# # 참: "~", [~], (~), {~}, 1
# # 거짓: "", [], (), {}, 0, None

# # city = "seoul"

# # if city:
# #     print('You aere in: ', city)
# # else:
# #     print('Please enter your city.')

# # 논리 연산자
# # and, or, not

# a = 100
# b = 60
# c = 15

# # print(a > b and b > c)
# # print(a > b or b > c)
# # print(not a > b)
# # print(not b > c)
# # print(not True)

# # 산술, 관계, 논리 우선순위
# # 산술 > 관계 > 논리 순서

# # print(3 + 12 > 7 + 3)
# # print(5 + 10 * 3 > 7 + 3 * 20)
# # print(5 + 10 > 3 and 7 + 3 == 10)
# # print(5 + 10 > 0 and not 7 + 3 == 10)

# score1 = 90
# score2 = 'A'

# # if score1 >= 90 and score2 == 'A':
# #     print("합격하셨습니다.")
# # else:
# #     print('불합격입니다.')

# id1 = 'gold'
# id2 = 'admin'
# id3 = 'super'

# # if id1 == 'gold' or id2 == 'admin':
# #     print("관리자 로그인 성공")

# # if id2 == 'admin' and id3 == 'super':
# #     print('최고 관리자 로그인 성공')

# is_work = False

# if is_work:
#     print('is work!')
    
# # 다중 조건문
# num = 90

# # if num >= 70:
# #     print(num)
# # elif num >= 60:
# #     print(num)
# # else:
# #     print('default num')
    
# # 중첩 조건문
# age = 27
# height = 175

# # if age >= 20:
# #     if height >= 170:
# #         print('A지망 지원 가능')
# #     elif height >= 160:
# #         print('B지망 지원 가능')
# #     else:
# #         print('지원 불가')
# # else:
# #     print('20세 이상 지원 가능')

# # in, not in
# q = [1, 2, 3]
# w = {7, 8, 9, 9}
# e = {'name': 'Kwon', 'city': 'seoul', 'grade': 'B'}
# r = (10, 12, 14)

# print(1 in q)
# print(6 in w)
# print(12 not in r)
# print('name' in e)
# print('seoul' in e.values())


# 코딩의 핵심은 조건 해결!
# while, for
v1 = 1

# while v1 < 11:
#     print(v1)
#     v1 += 1

# for v2 in range(1, 11, 2):
#     print(v2)

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
    
# print(sum1)
# print(cnt1)

# print(sum(range(1, 101)))
# print(sum(range(1, 101, 3)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

names = ['Kim', 'Kwon', 'Park', 'Cho', 'Lee', 'Choi']

# for name in names:
#     print(name)

lotto_numbers = [11, 19, 21, 28, 36, 37]

# for number in lotto_numbers:
#     print(number)

word = 'dreams'

# for s in word:
#     print(s)

my_info = {
    'name': 'Kwon',
    'age': 25,
    'city': 'Seoul'
}

# for key in my_info:
#     print(f'{key}: {my_info[key]}')

# for val in my_info.values():
#     print(val)

name = 'HenRY'

# for n in name:
#     if n.isupper():
#         print(n)
#     else:
#         print(n.upper())
        
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# break
# for num in numbers:
#     if num == 33:
#         print('found 33!')
#         break
#     else:
#         print('not found..', num)

# continue
lt = ['1', 2, 5, True, 4.3, complex(4)]

# for v in lt:
#     if type(v) is float:
#         continue
    # print(type(v))
    # print('multiple by 2: ', v * 3)
    
# for-else

# for num in numbers:
#     if num == 29:
#         print('found 33!')
#         break
#     else:
#         print('not found...', num)
# else:
#     print('not found 39...')

# flag 사용
f = True

# while f:
#     for v in numbers:
#         if v == 33:
#             print('found 33!')
#             f = False
#         print('not found...', v)

# else 구문(반복문이 정상적으로 수행된 경우 else block 수행)
# i = 1

# while i <= 10:
#     print(i)
#     if i == 6:
#         break
#     i += 1
# else:
#     print('else block run!')

# j = 1

# while j <= 10:
#     print(j)
#     if j == 11:
#         break
#     j += 1
# else:
#     print('else block run!')

# 중첩 for 문 구구단 출력
# for i in range(1, 10):
#     for j in range(1, 11):
#         print('{:4d}'.format(i * j), end='')
#     print()

# 자료 구조 변환
name = 'Niceman'
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))

# 순서 x
print(set(reversed(name)))