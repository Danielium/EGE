#2
# from itertools import product, permutations
# def f(x, y, w, z):
#     return y and (x or z) or (not (y or z)) or w
# for x1, x2, x3, x4 in product([0, 1], repeat = 4):
#     t = (
#         (1, x1, 0, 1, 0),
#         (x2, 1, 0, x3, 0),
#         (0, 0, x4, 1, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xywz', r=4):
#             if all(f(**dict(zip(p,l))) == l[-1] for l in t):
#                 print(*p)

#5
# for n in range(100):
#     b = bin(n)[2:]
#     if b.count('1') % 2 == 0: b = '1' + b[:-2] + '01'
#     if b.count('1') % 2 != 0: b = '1' + b[2:] + '10'
#     r = int(b, 2)
#     print(n, r)


#6
# from turtle import *
# tracer(0)
# m = 20
# screensize(10000, 10000)
# for i in range(4):
#     fd(16*m)
#     rt(90)
#     fd(18*m)
#     rt(90)
# up()
# rt(90)
# fd(10*m)
# lt(90)
# fd(10*m)
# down()
# for i in range(4):
#     fd(15*m)
#     rt(90)
# up()
# fd(1*m)
# lt(90)
# fd(1*m)
# rt(90)
# down()
# for i in range(7):
#     fd(12*m)
#     rt(90)
# up()
# for x in range(-20, 50):
#     for y in range(-40, 50):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# exitonclick()



#7
# print(400*1024*8)
# print(3276800/(265*2084))


#8
# from itertools import product
# count = 0
# for i in product('БГДНОУШ', repeat = 6):
#     s = ''.join(i)
#     count += 1
#     if count % 2 != 0 and s[0] != 'Б' and s.count('Н') >= 2 and s.count('У') == 0:
#         print(count, s)


#9
#сделал в exel


#11
# print((2782 * 8192)/1024)

#12
# s = 86 * '8'
# while '1111' in s or '8888' in s:
#     if '1111' in s: s = s.replace('1111', '8', 1)
#     else: s = s.replace('8888', '11', 1)
# print(s)



#13
# from ipaddress import *
# m = 0
# net = ip_network('203.155.64.98/203.155.64.0', 0)
# for ip in net:
#     m = max(m, f'{ip:b}'.count(1))
# print(m)



#14
# n = 1*3**37 + 2*3**23 + 3 * 3 ** 20 + 4 * 3 ** 4 + 5 * 3 ** 3 + 4 + 5
# c = []
# while n > 0:
#     c += [n%9]
#     n //= 9
# print(c.count(0))


#15
# def f(x, y, a):
#     return (2*x + y != 150) or (x not in range(50, 71)) or (a > y)
# print(min(a for a in range(1, 500) if all(f(x, y, a) == 1 for x in range(1, 500) for y in range(1, 500))))


#16
# def f(n):
#     if n <= 1: return 1
#     elif n > 1 and n % 2 == 0: return 3 * n + f(n-1)
#     else: return 2 * f(n-3)
# print(f(30))


#17
# a = [int(x) for x in open('file')]
# c = []
# for i in range(len(a) - 2):
#     if ((a[i] * a[i+1] * a[i + 2]) % 7 == 0) and ((a[i] + a[i+1] + a[i + 2]) % 10 == 5):
#         c += [a[i] + a[i+1] + a[i + 2]]
# print(len(c), max(c))


#19-21
# def f(a, b, m):
#     if (a + b) >= 65: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*3, b, m-1), f(a, b*3, m-1)]
#     return any(h) if m % 2 != 0 else all(h)
# print([s for s in range(1, 59) if f(6, s, 2)])  # тут ответ 7,
# # чтобы его получить надо поменять all на any,
# # тк ходит после НЕУДАЧНОГО хода Пети
# print([s for s in range(1, 59) if not f(6, s, 1) and f(6, s, 3)])
# print([s for s in range(1, 59) if not f(6, s, 2) and f(6, s, 4)])



#23
# def f(x, end):
#    if x < end: return 0
#    if x == end: return 1
#    return f(x-1, end) + f(x//2, end)
# print(f(89, 30) * f(30, 7))


#24
# a = [x for x in open('file').readline()]
# maxlen = 0
# curlen = 0
# for i in range(len(a) - 1):
#     if a[i] != a[i+1] and a[i] != a[i-1]:
#         curlen += 1
#         maxlen = max(maxlen, curlen)
#     else: curlen = 0
# print(maxlen)


