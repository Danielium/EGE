#2
# from itertools import product, permutations
# def f(x, y, w, z):
#     return ((1==w)==((not((w and x) or y)))) <= z
# for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 in product([0, 1], repeat=10):
#     t = (
#         (x1, x2, 1, x3, 0),
#         (1, x4, 1, x5, 0),
#         (0, 1, 0, 0, 1),
#         (1, x6, 1, x7, 1),
#         (x8, x9, 1, x10, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xywz', r=4):
#             if all(f(**dict(zip(p, l)))==l[-1] for l in t):
#                 print(*p)


#5
# for n in range(45, 300):
#     d = bin(n)[2:]
#     if n%2==0: d = bin(n)[2:] + '0'*(len(d)-d.count('1'))
#     if n%2==1: d = '1'*(len(d)-d.count('0'))+bin(n)[2:]
#     r = int(d, 2)
#     print(n, r, d)


#6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m=20
# for i in range(6):
#     fd(7*m)
#     rt(120)
# up()
# fd(3*m)
# rt(90)
# down()
# for i in range(8):
#     fd(5*m)
#     rt(90)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*m, y*m)
#         dot(3, 'red')
#
# update()
# exitonclick()

#7
# a = 2*44100*32
# print((50*1024*1024*8)/a)

#8
# from itertools import permutations
# c=0
# for i in permutations('КАБИНЕТ',r=7):
#     s = ''.join(i)
#     if s[-1] not in 'АИЕ':
#         c+=1
# print(c)

#12
# for n in range(30, 10000):
#     s = '8'+n*'4'
#     while '4444' in s or '844' in s or '84' in s:
#         if '4444' in s: s=s.replace('4444', '884', 1)
#         if '844' in s: s=s.replace('844', '488', 1)
#         if '84' in s: s=s.replace('84', '3343', 1)
#     if len(s)>=20:
#         break
# print(n)

#13
# from ipaddress import *
# net = ip_network('192.168.76.160/255.255.255.240')
# c=0
# k=0
# for ip in net:
#     c+=1
#     if c%2==0 and f'{ip:b}'[-8:].count('1')%2==0: k+=1
# print(k)


#15
# from itertools import combinations
# def f(x):
#     b = 101 <= x <= 143
#     c = 144 <= x <= 199
#     a = a1 <= x <= a2
#     return a<=(b or c)
# ox = [x*0.25 for x in range(101*4, 199*4)]
# m=[]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         m.append(a2-a1)
# print(max(m))

#дальше не из варика яндекса, тк варик яндекса бред

#16
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n<10:return n
#     return 3*n+g(n-2)
#
# @lru_cache(None)
# def g(n):
#     if n<10: return n
#     if n>9: return n - 2 + f(n-1)
#
# for x in range(1, 2204):
#     f(x)
#     g(x)
# print(f(2204)-g(2200))


