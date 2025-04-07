# from itertools import product, permutations
# def f(w, x, y, z):
#     return (y <= x) and (not w) and z
# for x1, x2, x3, x4 in product([0, 1], repeat = 4):
#     t = (
#         (1, 0, 1, 1, 1),
#         (1, 0, x1, 1, 1),
#         (x2, x3, x4, 1, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('wxyz', r=4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)

# for n in range(1, 100):
#     b = bin(n)[2:]
#     if b.count('1') % 2 == 0: b += '11'
#     if b.count('1') % 2 != 0: b += '01'
#     r = int(b, 2)
#     print(n, b, r)


# from turtle import *
# tracer(0)
# screensize(2000, 2000)
# m = 30
# for n in range(5):
#     fd(8*m)
#     rt(90)
#     fd(11*m)
#     rt(90)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*m, y*m)
#         dot(3, 'red')
# update()
# exitonclick()


# from itertools import product
# x=0
# for i in list((product('БЕНРСТЬЯ', repeat=5))):
#     x+=1
#     s = ''.join(i)
#     if x%2==0 and s[0]=='Р' and s.count('Ь')==0:
#         print(x, s)

# c = 0
# for line in open('9test'):
#     n = sorted([int(x) for x in line.split()])
#     okf = [x for x in n if x%10==5]
#     if (2*(n[-1] + n[-2]) > 3*(n[0]+n[1]+n[2])) and len(okf) >= 2:
#         c += 1
# print(c)

# s = 68*'9'
# while '22222' in s or '9999' in s:
#     if '22222' in s: s = s.replace('22222', '99', 1)
#     else: s=s.replace('9999', '29', 1)
# print(s.count('9'))



# from ipaddress import *
# c=0
# net = ip_network('228.172.236.0/255.255.240.0', 0)
# for ip in net:
#     n = bin(int(ip))[2:].zfill(32)
#     if n.count('1')%5!=0:
#         c+=1
# print(c)


# n = 4**644 + 4**322 + 16**35 - 64**3
# c = []
# while n > 0:
#     c += [n%4]
#     n//=4
# print(c.count(3))


# def f(a, x, y):
#     return (x<= 19) or (y < 2*x + a - 50) or (y>17)
# print(min(a for a in range(1, 200) if all(f(a, x, y) == 1 for x in range(1, 100) for y in range(1, 100))))


# def f(n):
#     if n>400: return n**n
#     if n <=400: return n + 6 + f(n+12)
# print(f(72)-f(108))


# def f(s, m):
#     if s >= 54: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 2, m - 1), f(s * 2, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
# print('19 -_-', [s for s in range(1, 54) if not f(s, 1) and f(s, 2)])
# print('20 -_-', [s for s in range(1, 281) if not f(s, 1) and f(s, 3)])
# print('21 -_-', [s for s in range(1, 281) if not f(s, 2) and f(s, 4)])



# def f(x, end):
#     if x == end: return 1
#     if x > end or x == 22: return 0
#     return f(x + 3, end) + f(x+4, end)
# print(f(16, 38))


# from fnmatch import fnmatch
# for i in range(0, 10**10, 2025):
#     if fnmatch(str(i), '21?3*145?5'):
#         print(i, i//2025)

# a = [int(x) for x in open('9test')]
# m = min(a)
# c = []
# for i in range(len(a)-1):
#     if a[i]%77 + a[i+1]%77 == m:
#         c+=[a[i]+a[i+1]]
# print(len(c), max(c))

# s = open('9test').readline()
# s = s.replace('+', '*').replace('**', ' ')
# print(max(len(a) for a in s.split()))




