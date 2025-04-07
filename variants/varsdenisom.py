# from itertools import product, permutations
# def f(w, x, y, z):
#     return y and (x or z) or (not (y or z)) or w
# for x1, x2, x3, x4 in product([0, 1], repeat=4):
#     t = (
#         (1, x1, 0, 1, 0),
#         (x2, 1, 0, x3, 0),
#         (0, 0, x4, 1, 0)
#     )
#     if len(t)==len(set(t)):
#         for p in permutations('wxyz', r=4):
#             if all(f(**dict(zip(p, l)))==l[-1] for l in t):
#                 print(*p)


# for x in range(1, 300):
#     n = bin(x)[2:]
#     if n.count('1') % 2 == 0:
#         n += '0'
#         n = '10' + n[2:]
#     else:
#         n += '1'
#         n = '11' + n[2:]
#     r = int(n, 2)
#     print(x, r)


# from turtle import *
# tracer(0)
# m = 20
# screensize(10000, 10000)
# for x in range(16):
#     fd(10*m)
#     rt(120)
#     fd(10*m)
#     rt(60)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# update()
# exitonclick()


# from itertools import product
# n = 0
# for i in product('ИРЩЮ',repeat=5):
#     n+=1
#     s = ''.join(i)
#     if s[0]=='Щ' and s[-1]=='И':
#         print(n, s)


# count = 0
# for line in open('9sdenisom'):
#     n = sorted([int(x) for x in line.split()])
#     if n[-1] < n[0]+n[1]+n[2]:
#         if (n[0]+n[1] == n[2]+n[3]) or (n[0]+n[2] == n[1]+n[3]) or (n[0]+n[3] == n[1]+n[2]):
#             count += 1
# print(count)


s = 170*'7'
while '777' in s:
    s = s.replace('77', '2', 1)
    s = s.replace('22', '7', 1)
print(s)