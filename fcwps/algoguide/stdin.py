# import sys
#
# for line in sys.stdin:
#     if 'exit' == line.rstrip():
#         break
#     print(f'processing message from sys.stdin {line}')
# print('done')

import fileinput

for fileiput_line in fileinput.input():
    if 'exit' == fileiput_line.rstrip():
        break
    print(f'processing message from fileinput.input() {fileiput_line}')
print('done')

# while True:
#     data = input('please enter the message:\n')
#     if 'exit' == data:
#         break
#     print(f'processing message from input {data}')
#
# print('done')
