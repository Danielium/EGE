#2
# from itertools import product, permutations
# def f(x, y, w, z):
#     return (not (x or y)) and (not w) or (not (z or w)) and y
# for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat = 8):
#     t = (
#         (x1, 1, x2, x3, 1),
#         (x4, x5, 1, x6, 1),
#         (x7, 1, x8, 1, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xywz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)

#5
# def f(n):
#     b = bin(n)[2:]
#     if b.count('1') % 2 == 0: b = '11' + b[2:] + '0'
#     elif b.count('1') % 2 != 0: b = '10' + b[2:] + '1'
#     r = int(b, 2)
#     return r
# print(max(f(n) for n in range(1, 50)))


#6
# from turtle import *
# screensize(10000, 10000)
# tracer(0)
# m = 20
# for i in range(9):
#     fd(22 * m)
#     rt(90)
#     fd(6*m)
#     rt(90)
# up()
# fd(1*m)
# rt(90)
# fd(5*m)
# lt(90)
# down()
# for i in range(9):
#     fd(53*m)
#     rt(90)
#     fd(75*m)
#     rt(90)
# up()
# for x in range(-40, 40):
#     for y in range(-40, 40):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# exitonclick()


#7
# v = 2764*1793*13
# packet = v * 148
# speed = 18349566
# print(packet/speed)


#8
# from itertools import product
# count = 0
# for i in product('01234567', repeat = 5):
#     s = ''.join(i)
#     if s[0] != '0' and s[0] not in '1357' and s[-1] not in '26' and s.count('7') <= 2:
#         count += 1
#         print(s)
# print(count)



#9
# count = 0
# for line in open('file'):
#     a = [int(x) for x in line.split()]
#     b = sorted([int(x) for x in line.split()])
#     if b[-1] < (b[0] + b[1] + b[2]):
#         if (a[0] + a[1] == a[2] + a[3]) or (a[0] + a[2] == a[1] + a[3])\
#             or (a[0] + a[3] == a[2] + a[1]):
#             print(a)
#             count += 1
# print(count)




#11
# pamyat_one = ((276 * 1024) / 862)
# v_bitah = 327 * 8
# print(v_bitah/10)



#12
# s = 136 * '9'
# while '22222' in s or '9999' in s:
#     if '22222' in s: s = s.replace('22222', '99', 1)
#     else: s = s.replace('9999', '2', 1)
# print(s)


#13
# from ipaddress import *
# count = 0
# net = ip_network('112.160.0.0/255.240.0.0', 0)
# for ip in net:
#     if f'{ip:b}'.count('1') % 5 == 0:
#         count += 1
# print(count)




#14
# for x in range(1, 2031):
#     c = []
#     n = 3 ** 100 - x
#     while n > 0:
#         c += [n % 3]
#         n //= 3
#     if c.count(0) == 5: print(x, c)


#15
# def d(n, m):
#     return n % m == 0
# def f(a, x):
#     return (not d(a, x)) <= (d(x, 14) <= (not d(x, 4)))
# print(max(a for a in range(1, 1000) if all(f(a, x) == 1 for x in range(1, 1000))))


#16
# from sys import *
# setrecursionlimit(2500)
# def f(n):
#     if n == 1: return 1
#     if n > 1: return (n+1) * f(n-1)
# print((f(2024)-3*f(2023))// f(2022))



#17
# a = [int(x) for x in open('file')]
# kr = [x for x in a if x % 32 == 0]
# count = 0
# m = 0
# for i in range(len(a) - 1):
#     if a[i] + a[i+1] < len(kr) and (a[i] < 0 or a[i+1] < 0):
#         count += 1
#         m = max(m, a[i] + a[i+1])
#         print(a[i], a[i+1])
# print(count, m)


#23
def f(x, end):
    if x == end: return 1
    if x > end: return 0
    return f(x+1, end) + f(x*2, end)
print(f(4, 8) * f(8, 10) * f(10, 15))