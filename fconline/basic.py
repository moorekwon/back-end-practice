# -*- coding: utf8 -*-

# import this
import sys

# encoding
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is hyojin kwon.')

# 변수 선언
myName = 'hyojin'

# 조건문
if myName == "hyojin kwon":
    print('Okay') # indent

# 반복문
# for i in range(1, 10):
#     for j in range(1, 10):
#         print('%d * %d = ' % (i, j), i * j)

# 함수 선언
def hello():
    print('안녕하세요. 반갑습니다.')

hello()

# class
class Cookie:
    pass
# 객체(instance) 생성
cookie = Cookie()
print(id(cookie))
print(dir(cookie))