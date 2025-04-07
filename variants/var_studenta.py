#2
# from itertools import product, permutations
# def f(x, y, w, z):
#     return ((((not y) <= (not w)) <= (not z)) <= x)
# for x1, x2, x3, x4, x5 in product([0, 1], repeat = 5):
#     t = (
#         (x1, 1, x2, 1, 0),
#         (0, 1, x3, 0, 1),
#         (x4, x5, 1, 0, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xywz', r=4):
#             if all(f(**dict(zip(p, l)))==l[-1] for l in t):
#                 print(*p)


#5
# def tr(x):
#     c = ''
#     while x > 0:
#         c += str(x%3)
#         x//=3
#     return c[::-1]
# nki = []
# for n in range(1, 100):
#     s = tr(n)
#     if n % 3==0:
#         s = '1'+s+'01'
#     else:
#         s += str(tr(((n%3)*5)))
#     r = int(s, 3)
#     if r < 299: nki.append(n)
# print(nki)

#6
# from turtle import *
# screensize(10000, 10000)
# tracer(0)
# m = 20
# fd(10*m)
# rt(90)
# fd(5*m)
# rt(90)
# fd(8*m)
# rt(90)
# fd(8*m)
# up()
# for x in range(-10, 30):
#     for y in range(-10, 30):
#         goto(x*m, y*m)
#         dot(3, 'blue')
# exitonclick()


#9
for line in open('9stud'):
    n = [int(x) for x in line.split()]
