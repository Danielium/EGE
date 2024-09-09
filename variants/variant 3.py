#2
# from itertools import product, permutations
# def f(w, x, y, z):
#     return (not x == (w and (not z))) and (y == (x and (not w)))
# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat = 6):
#     t = (
#         (x1, x2, 0, x3, 1),
#         (x4, 0, x5, 0, 1),
#         (0, x6, 1, 0, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('wxyz', r=4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)

#5
# for n in range(1, 50):
#     b = bin(n)[2:]
#     if b.count('1') % 2 == 0: b = '11'+b[2:]+'0'
#     else: b = '10'+b[2:]+'1'
#     r = int(b, 2)
#     print(r)


#8
# from itertools import permutations
# count = 0
# for i in set(permutations('СОВЕСТЬ')):
#     s = ''.join(i)
#     for g in 'ОЕЬ': s = s.replace(g, 'g')
#     for sog in 'СВТ': s = s.replace(sog, 's')
#     if not('ss' in s and 'gg' in s):
#         count += 1
# print(count)

#12
# for n in range(4, 100):
#     s = '2' + n * '5'
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '5', 1)
#         if '355' in s:
#             s = s.replace('355', '52', 1)
#         if '555' in s:
#             s = s.replace('555', '3', 1)
#     if s.count('3') == 3:
#         print(n)


#13
from ipaddress import *
for a in range(256):
    net = ip_network(f'246.81.65.{a}/255.255.255.224')
    for ip in net:


