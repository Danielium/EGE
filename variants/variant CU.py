# from itertools import product, permutations
# def f(x, y, z):
#     return (x == y) or ((z or y) <= x)
# for x1, x2, x3 in product([0, 1], repeat = 3):
#     t = (
#         (x1, 1, x2, 0),
#         (x3, 1, 1, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyz', r=3):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)

# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 20
# for i in range(7):
#     fd(4*m)
#     rt(90)
#     fd(3*m)
#     rt(90)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(m*x, y*m)
#         dot(3, 'blue')
# exitonclick()
# update()


# s = 800 * 1024 * 8
# xy = 1000*800
# print(s)
# print(8*xy)
# print(2**8)


# from itertools import product
# x = 0
# for i in product('АДМТ', repeat = 5):
#     x += 1
#     s = ''.join(i)
#     print(x, s)


# c=0
# for line in open('file'):
#     n = sorted([int(x) for x in line.split()])
#     np = [x for x in n if n.count(x) == 1]
#     if len(np) == 5 and (n[0] + n[-1])*2 <= (n[1] + n[2] + n[3]):
#         c += 1
#         print(n)
# print(c)


# from ipaddress import *
# net = ip_network('192.138.245.125/255.255.240.0', 0)
# print(net)


# n = 36**7 + 6**30 - 12
# c = []
# while n > 0:
#     c+=[n%6]
#     n//=6
# print(c.count(5))


# def f(a, x, y):
#     return (x+2*y > 16) or (x+y<=a)
# print(min(a for a in range(0, 200) if all(f(a, x, y) for x in range(200) for y in range(200))))


# def f(n):
#     if n==1: return 1
#     if n==2: return 2
#     return 3 * f(n-1) - f(n-2)
# print(f(8))


# def f(s, m):
#     if s >= 41: return m%2==0
#     if m == 0: return 0
#     h = [f(s+2, m-1), f(s+3, m-1), f(s*2, m-1)]
#     return any(h) if m%2!=0 else all(h) #тут меняешь на any, если после неудачного хода
# print('19)', [s for s in range(1, 40) if f(s, 2)])
# print('20)', [s for s in range(1, 40) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 40) if not f(s, 2) and f(s, 4)])

# def f(x, end):
#     if x == end: return 1
#     if x > end: return 0
#     return f(x+1, end) + f(x+4, end) + f(x*2, end)
# print(f(1, 10)*f(10, 24))


# from fnmatch import fnmatch
# for x in range(2024, 10**7, 2024):
#     if fnmatch(str(x), '2?3*96'):
#         print(x, x//2024)


# for x in range(10000, 100000):
#     sn = x//10000 + (x//100)%10 + (x%10)
#     sch = (x//1000)%10 + (x//10)%10
#     s = str(min(sn, sch)) + str(max(sn, sch))
#     if s == '621':
#         print(x)

# n = [int(x) for x in open('17.txt')]
# c = []
# for i in range(len(n)-1):
#     if (n[i] % 4 == 0) + (n[i+1] % 4 == 0) >= 1:
#         if (n[i] + n[i+1]) % 7 == 0:
#             c += [n[i] + n[i+1]]
#             print(n[i], n[i+1])
# print(len(c), max(c))

