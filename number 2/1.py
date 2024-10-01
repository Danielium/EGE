#from itertools import product, permutations
#
#def f (x, y, z, w, u):
#    return ((z <= w) and (y == (not x))) <= (u == (y or z))
#
#
#for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat = 8):
#    t.t.txt = (
#        (0, x1, 0, 0, 0, 0),
#        (0, x2, x3, 0, 0, 0),
#        (x4, 0, 0, 0, x5, 0),
#        (0, 0, x6, x7, x8, 0),
#    )
#    if len(t.t.txt) == len(set(t.t.txt)):
#        for p in permutations('xyzwu', r = 5):
#            if all(f(**dict(zip(p, m))) == m[-1] for m in t.t.txt):
#                print(*p)
# № 13089



# from itertools import permutations, product

# def f(w, x, y, z):
#     return ((x and (not y)) <= (z and w)) and ((y <= z) or (w <= x))
# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat = 6):
#     t.t.txt = (
#         (x1, x2, 1, 1, 0),
#         (1, x3, 1, x4, 0),
#         (x5, 0, x6, 1, 0)
#     )
#     if len(t.t.txt) == len(set(t.t.txt)):
#         for p in permutations('wxyz', r = 4):
#             if all(f(**dict(zip(p, m))) == m[-1] for m in t.t.txt):
#                 print(*p)
# № 12670



# from itertools import permutations, product
#
# def f (w, x, y, z):
#     return (x <= y ) and z and (not w)
#
# for x1, x2, x3, x4 in product([0, 1], repeat=4):
#     t.t.txt = (
#         (0, 1, x1, 1, 1),
#         (x2, 1, x3, x4, 1),
#         (0, 1, 1, 1, 1)
#     )
#     if len(t.t.txt) == len(set(t.t.txt)):
#         for p in permutations('wxyz', r = 4):
#             if all(f(**dict(zip(p, m))) == m[-1] for m in t.t.txt):
#                 print(*p)
# № 11220



# from itertools import permutations, product
#
# def f(w, x, y, z):
#     return ((x and (not y)) or (x == z) or w)
#
#
# for x1, x2, x3, x4 in product([0, 1], repeat = 4):
#     t.t.txt = (
#         (x1, x2, 0, 1, 0),
#         (1, 0, x3, 1, 0),
#         (1, 1, 0, x4, 0)
#     )
#     if len(t.t.txt) == len(set(t.t.txt)):
#         for p in permutations('wxyz', r=4):
#             if all(f(**dict(zip(p, m))) == m[-1] for m in t.t.txt):
#                 print(*p)

# № 9733



# from itertools import product, permutations
#
# def f(w, x, y, z):
#     return (x <= y) and ((not y) == z) and w
#
#
# for x1, x2, x3, x4, x5, x6 in product ([0, 1], repeat = 6):
#     t.t.txt = (
#         (x1, 1, x2, x3, 1),
#         (x4, 1, 1, x5, 1),
#         (x6, 1, 1, 1, 1)
#     )
#     if len(t.t.txt) == len(set(t.t.txt)):
#         for p in permutations('wxyz', r=4):
#             if all(f(**dict(zip(p, m))) == m[-1] for m in t.t.txt):
#                 print(*p)
# № 9532


# from itertools import product, permutations
#
# def f(w, x, y, z):
#     return ((y and (x == (not z))) <= w) and (z <= y)
# for x1, x2, x3, x4, x5 in product([0, 1], repeat = 5):
#     t.t.txt = (
#         (0, 0, x1, x2, 0),
#         (0, x3, 0, 0, 0),
#         (1, x4, x5, 1, 0)
#     )
#     if len(t.t.txt) == len(set(t.t.txt)):
#         for p in permutations('wxyz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t.t.txt):
#                 print(*p)


# from itertools import product, permutations
#
# def f(w, x, y, z):
#     return y and (x or z) or (not(y or z)) or w
#
# for x1, x2, x3, x4 in product([0, 1], repeat=4):
#     t.t.txt = (
#         (1, x1, 0, 1, 0),
#         (x2, 1, 0, x3, 0),
#         (0, 0, x4, 1, 0)
#     )
#     if len(t.t.txt) == len(set(t.t.txt)):
#         for p in permutations('wxyz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t.t.txt):
#                 print(*p)


# from itertools import product, permutations
#
# def f(w, x, y, z):
#     return (w or x or y) <= ((y or z) and x or y and (w or z))
#
# for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
#     t.t.txt = (
#         (0, 0, 0, x1, 0),
#         (x2, 1, 1, x3, 0),
#         (x4, 1, x5, 1, 0)
#     )
#     if len(t.t.txt) == len(set(t.t.txt)):
#         for p in permutations('wxyz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t.t.txt):
#                 print(*p)


# from itertools import product, permutations
#
# def f(w, x, y,z):
#     return (w or y) and (x <= (not z)) and (not w)
# count = 0
# for x1, x2, x3, x4, x5 in product([0, 1], repeat = 5):
#     t.t.txt = (
#         (x1, 0, x2, 0, 1),
#         (1, x3, x4, x5, 1),
#         (1, 1, 0, 0, 1)
#     )
#     if len(t.t.txt) == len(set(t.t.txt)):
#         for p in permutations('wxyz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t.t.txt):
#                 count = len(set(p))
# print(count)




# from itertools import permutations, product
#
# def f1(w, x, y, z):
#     return (w <= y) == (x and z)
# def f2(w, x, y, z):
#     return (not x) or (not y) or (not z) or w
# def f3(w, x, y, z):
#     return (z or w) and y and x
# t = (
#     (1, 0, 1, 0, 1),
#     (0, 1, 1, 1, 0),
#     (1, 1, 1, 0, 1)
# )
#
#
#
#
# for p in permutations('wxyz', r=4):
#     if f1(**dict(zip(p, t[0]))) == t[0][-1] and f2(**dict(zip(p, t[1]))) == t[1][-1] and f3(**dict(zip(p, t[2]))) == t[2][-1]:
#         print(*p)



# from itertools import product, permutations
# def f(w, x, y, z):
#     return ((x <= y) == (w <= x)) and (z <= w)
# for x1, x2, x3, x4 in product([0,1], repeat = 4):
#     t = (
#         (1, 0, 0, 1, 1),
#         (1, x1, x2, 0, 1),
#         (x3, 0, 1, x4, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('wxyz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)






# from itertools import product, permutations
# def f1(x, y, w, z):
#     return (w <= y) == (x and z)
# def f2(x, y, w, z):
#     return (not x) or (not y) or (not z) or w
# def f3(x, y, w, z):
#     return (z or w) and y and x
# t = (
#     (1, 0, 1, 0, 1),
#     (0, 1, 1, 1, 0),
#     (1, 1, 1, 0, 1)
# )
# for p in permutations('xywz', r=4):
#     if f1(**dict(zip(p, t[0]))) == t[0][-1] and f2(**dict(zip(p, t[1]))) == t[1][-1] and f3(**dict(zip(p, t[2]))) == t[2][-1]:
#         print(*p)



# from itertools import product, permutations
# def f(w, x, y, z):
#     return (not (x <= z)) or (y == w) or y
# for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat = 7):
#     t = (
#         (1, 0, x1, x2, 0),
#         (x3, 1, 0, x4, 0),
#         (0, x5, x6, x7, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('wxyz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)


# from itertools import product, permutations
# def f(x, y, w, z):
#     return (x or y and (not z)) and (not w)
# t = (
#     (1, 0, 0, 0, 1),
#     (0, 0, 1, 0, 1),
#     (0, 1, 0, 1, 0)
# )
# for p in permutations('wxyz', r = 4):
#     if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#         print(*p)


# from itertools import product, permutations
# def f(x, y, w, z):
#     return ((z <= (not (y <= x))) or w)
# for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat = 7):
#     t = (
#         (x1, 1, x2, x3, 0),
#         (x4, x5, 0, 0, 0),
#         (x6, 0, 1, x7, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xywz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)



# from itertools import product, permutations
# def f(x, y, w, z):
#     return ((w <= y) <= x) or (not z)
# for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat = 7):
#     t = (
#         (x1, x2, 1, x3, 0),
#         (x4, 0, x5, x6, 0),
#         (x7, 1, 0, 0, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xywz', r = 4):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p)



