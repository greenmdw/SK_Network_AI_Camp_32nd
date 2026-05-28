# 2026.05.25 혼공파 공부 (chapter 4)
list_1 = ['a', 'b', 'c']
# # for i in range(3):
# #     print('{}번째 값: {}'.format(i, list[i]))

# print(enumerate(list_1))
# print(list(enumerate(list_1)))

# for i, value in enumerate(list_1):
#     print('{}번째 값: {}'.format(i, value))

# example = {
#     1 : 'ABC',
#     2 : 'DEF',
#     3 : 'HIR'
# }

# print(example)
# print(example.items())
# for key, element in example.items():
#     print(key, element)

# array = []
# for i in range (0, 20, 2):
#     array.append(i * i)
# print(array)

# array = [i * i for i in range(0, 20, 2)]
# print(array)

# array = ["사과", '배', '포토', '초콜렛']
# output = [fruit 
#           for fruit in array 
#           if fruit != "초콜렛"]
# print(output)

# number = int(input('정수 입력: '))
# if number % 2 == 0:
#     print("\n".join([
#         '입력한 문자열은 {}',
#         '{}은 짝수입니다.'
#     ]).format(number, number))
# else:
#     print('\n'.join([
#             '입력한 문자열은 {}',
#         '{}은 짝수입니다.'
#     ]).format(number, number))

number = [1, 2, 3, 4, 5, 6]
r_num = reversed(number)

# print(r_num)
# # print(list(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))

# 10진수와 2진수 변환
# print("{:b}".format(10))        # 1010 : 10을 2진수로 전환
# print(int('1010', 2))           # 10    : 1010이 2진수 이니 10진수로 전환

# # 10진수와 8진수 변환
# print("{:o}".format(10))        # 12
# print(int('12', 8))             # 10

# # 10진수와 16진수 변환
# print("{:x}".format(10))        # a
# print(int('10', 16))            # 16

# print('안녕하세요안'.count('안'))

# 1 ~ 100 사이 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고, 
# 그 숫자들의 합을 구해라
output = []

for i in range(100):
    bin = "{:b}".format(i + 1)
    if bin.count('0') == 1:
        output.append(bin)
    else:
        continue

for i in range(len(output)):
    print("{}: {}".format(il, "{:b}".format(il + 1)))

output = [num for num in ]