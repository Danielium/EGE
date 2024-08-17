#2
# from itertools import product, permutations
# def f(x, y, w, z):
#     return (not (y <= x)) or (y == w) or z
# for x1, x2, x3, x4, x5, x6 in product([0,1], repeat = 6):
#     t = (
#         (x1, x2, 1, 1, 0),
#         (x3, x4, 1, x5, 0),
#         (0, 1, x6, 1, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xywz', r=4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)


#8
# from itertools import product
# number = 0
# count = 0
# for i in product('АЕИКЛПР', repeat = 6):
#     s = ''.join(i)
#     number += 1
#     if number % 2 == 0 and s[0] != 'К' and s.count('И') >= 2:
#         count += 1
#         print(number, s)
# print(count)



#9
count = 0
for line in open('file'):
    a = [int(x) for x in line.split()]
    dv = [x for x in a if a.count(x) == 2]
    if len(dv) == 6 and min(a) not in dv:
        count += 1
        print(dv)
print(count)


