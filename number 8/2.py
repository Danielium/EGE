# from itertools import permutations
#
#
# count = 0
# a = list(permutations('01234567', r=5))
# f = list(permutations('0246', r=2)) + list(permutations('1357', r=2))
# for x in a:
#     x = ''.join(x)
#     if x.count('1') == 0 and x[0] != '0':
#         if all(''.join(s) not in x for s in f):
#             count += 1
# print(count)
# 180
#


# Сколько существует восьмеричных шестизначных чисел, не содержащих
# в своей записи цифру 3, в которых все цифры различны и хотя бы две чётные стоят рядом?
# from itertools import permutations
# count = 0
# for x in permutations(range(8), r=6):
#     if x.count(3) == 0 and x[0] != 0 and any(x[i] % 2 == 0 and x[i+1] % 2 == 0 for i in range(5)):
#         count += 1
# print(count)
# 3852


#Сколько существует 4-разрядных четверичных чисел, в которых хотя бы одна цифра встречается не менее двух раз?
# from itertools import product
# count = 0
# for x in product('0123', repeat=4):
#     if x[0] != '0' and (x.count('0') >= 2 or x.count('1') >= 2 or x.count('2') >= 2 or x.count('3') >= 2):
#         count += 1
# print(count)
# 174

# Сколько существует десятичных пятизначных чисел, не содержащих в своей записи цифру 5
# , в которых все цифры различны и никакие две чётные или две нечётные цифры не стоят рядом?
# from itertools import permutations
# count = 0
# for x in permutations(range(10), r=5):
#     if x[0] != 0 and x.count(5) == 0 and all(x[i] % 2 != x[i + 1] % 2 for i in range(4)):
#         count += 1
#         print(x)
# print(count)
# 1056

# from itertools import permutations
# count = 0
# for x in permutations(range(8), r=5):
#     if x[0] != 0 and x.count(1) == 0 and all(x[i] % 2 != x[i+1] % 2 for i in range(4)):
#         count += 1
#         print(x)
# print(count)


# from itertools import permutations
# count = 0
# a = list(permutations('0123456789abcdef', r=3))
# b = list(permutations('02468ace', r=2)) + list(permutations('13579bdf', r=2))
# for x in a:
#     if all(''.join(s) not in ''.join(x) for s in b) and x[0] != '0':
#         count += 1
# print(count)


# from itertools import product
# l = list(product('01234567', repeat = 5))
# count = 0
# for s in l:
#     if s.count('6') == 1 and all(n not in ''.join(s) for n in ['16', '36', '56', '76', '67', '65', '63', '61']) and s[0] != '0':
#         count+=1
# print(count)

# from itertools import permutations
# l = list(permutations('01234567', r=5))
# sp = list(permutations('0246', r=2)) + list(permutations('1357', r=2))
# count = 0
# for i in l:
#     if i[0] != '0' and i.count('1') == 0 and all(''.join(s) not in ''.join(i) for s in sp):
#         count += 1
# print(count)


# from itertools import product
# l = list(product('012345678', repeat=5))
# count = 0
# for s in l:
#         if s[0] != '0' and s.count('5') == 1 and all(x not in ''.join(s) for x in ['00', '11','22', '33', '44', '55', '66', '77', '88']):
#             count += 1
# print(count)


# from itertools import permutations
# l = list(permutations('01234567', r=6))
# c = list(permutations('0246', r=2))
# count = 0
# for s in l:
#     if s[0] != '0' and s.count('3') == 0 and any(''.join(i) in ''.join(s) for i in c):
#         count += 1
# print(count)


# from itertools import product
# l = list(product('012345', repeat = 7))
# count = 0
# for s in l:
#     if s[0] != '0' and s.count('2') == 1 and all(k not in ''.join(s) for k in ['20', '22', '24', '42', '02']):
#         count += 1
#         print(''.join(s))
# print(count)


# from itertools import product
# count = 0
# l = list(product('0123456789abcdef', repeat = 4))
# a = list(product('02468ace', repeat = 2)) + list(product('13579bdf', repeat = 2))
# for s in l:
#     if s[0] != '0' and s.count('9') == 1 and all(''.join(i) not in ''.join(s) for i in a):
#         print(s)
#         count += 1
# print(count)


# from itertools import product
# count = 0
# l = list(product('0123456', repeat = 6))
# for s in l:
#     if s[0] != '0' and int(s[-1]) > 3 and sum(s.count(c) for c in '0246') == sum(s.count(c) for c in '135'):
#         count += 1
# print(count)

# from itertools import permutations
# count = 0
# a = list(permutations('0123456789abcdef', r=5))
# b = list(permutations('02468ace', r=2)) + list(permutations('13579bdf', r=2))
# for x in a:
#     if all(''.join(s) not in ''.join(x) for s in b) and x[0] != '0':
#         count += 1
# print(count)
# print(697 - 398)

from itertools import permutations, product
count = 0
a = list(permutations('0123456789abcdef', r = 3))
f = list(product('02468ace', repeat = 2)) + list(product('13579bdf', repeat = 2))
for x in a:
    if all(''.join(s) not in ''.join(x) for s in f) and x[0] != '0':
        count += 1
print(count)



