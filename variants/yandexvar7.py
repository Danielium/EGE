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

#17
# def sc(x):
#     return sum(map(int, str(abs(x))))
# n = [int(x) for x in open('t.txt', encoding='utf-8-sig')]
# m = max(k for k in n if len(str(abs(k))) == 3)
# sp = []
# for i in range(len(n) - 1):
#     if (sc(abs(n[i])) % 5 == 0) != (sc(abs(n[i+1])) % 5 == 0):
#         if abs(n[i]**2 - n[i+1]**2) >= m**3:
#             sp.append(n[i] + n[i+1])
# print(len(sp), max(sp))

#19-21
# def f(a, b, m):
#     if a+b >= 189: return m%2==0
#     if m == 0: return 0
#     if a>=b:
#         h = [f(a+b, b, m-1), f(a, a+b, m-1), f(a, a, m-1)]
#     if a<b:
#         h = [f(a+b, b, m-1), f(a, a+b, m-1), f(b, b, m-1)]
#     return any(h) if m%2!=0 else all(h)
# print([s for s in range(1, 184) if f(5, s, 2)]) # 60
# print([s for s in range(1, 184) if not f(5, s, 1) and f(5, s, 3)])
# print([s for s in range(1, 184) if not f(5, s, 2) and f(5, s, 4)])

#23
# def pc2(x):
#     return int(str(x**2)[0])
# def sc(x):
#     return sum(map(int, str(x)))
# def f(x, end):
#     if x==end: return 1
#     if x < end: return 0
#     return f(x-pc2(x), end)+f(x-sc(x), end)
# print(f(32, 1))

#25
# from fnmatch import fnmatch
# for x in range(0, 10**10, 42):
#     if fnmatch(str(x), '48*15*0'):
#         print(x, x//42)

#27
clustersA = [[], []]
clustersB = [[], [], []]
for line in open('27_А.txt'):
    x, y = [float(k) for k in line.split()]
    if x > 0: clustersA[0].append([x, y])
    else: clustersA[1].append([x, y])
for line in open('27_Б.txt'):
    x, y = [float(k) for k in line.split()]
    if y<x: clustersB[0].append([x, y])
    if y<-x-0.1: clustersB[1].append([x, y])
    else: clustersB[2].append([x, y])
def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]
centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]
pxA = sum(x for x, y in centersA)/2 * 10000
pyA = sum(y for x, y in centersA)/2 * 10000
pxB = sum(x for x, y in centersB)/3 * 10000
pyB = sum(y for x, y in centersB)/3 * 10000
print(int(abs(pxA)), int(abs(pyA)))
print(int(abs(pxB)), int(abs(pyB)))
