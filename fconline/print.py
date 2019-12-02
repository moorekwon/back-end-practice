# -*- coding: utf8 -*-

print('Hello python!')
print("Hello python!")
print("""Hello python!""")
print('''Hello python!''')
print('')

# separator option
# print('T', 'E', 'S', 'T', sep='')
# print('2019', '02', '19', sep='-')
# print(2019, 02, 19, sep='-')

#end option
# print('welcome to', end='')
# print('the black paradise', end='')

#format
print('{} and {}'.format('you', 'me'))
print("{0} and {1} and {0}".format('you', 'me'))
print("{a} are {b}".format(a='you', b='me'))
print('')

# %s: 문자, %d: 정수, %f: 실수
print("%s's favorite number is %d" % ('Hyojin', 7))
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))
print('')

#escape code
# \n: 개행
# \t: 탭
# \\, \', \": 문자
# \r: 캐리지 리턴
# \f: 폼 피드
# \a: 벨 소리
# \b: 백 스페이스
# \000: 널 문자
print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n\n')
print('test')
print('\t\t\ttest')


