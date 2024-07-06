# А наибольшее (А = 1): f == f_usl
# А наименьшее (А = 0): f != f_usl






# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     D = 7 <= x <= 68
#     C = 29 <= x <= 100
#     A = 0
#     f = D <= (((not C) and (not A)) <= (not D))
#     if f != 1:
#         print(x)
# 29 - 7 = 22

# for x in [k * 0.25 for k in range (-10000, 10000)]:
#     p = 13 <= x <= 19
#     q = 17 <= x <= 23
#     a = 1
#     #f = 1-(1-p <= q) <= (a <= (1-q <= p))
#     f = (not(not p) <= q) <= (a <= (not q) <= p)
#     if f != 0:
#         print(x)
# 23 - 13 = 10


# for x in [k * 0.25 for k in range(-10000, 10000)]:
#    P = 3 <= x <= 15
#    Q = 14 <= x <= 25
#    A = 1
#    f = (P == Q) <= (not A)
#    if f != 0:
#        print(x)
# отрезки 10 и 11, выбираем 11


# for x in [k * 0.25 for k in range (-10000, 10000)]:
#    B = 23 <= x <= 37
#    C = 41 <= x <= 73
#    A = 0
#    f = (not((not B) <= C) <= A)
#    if f != 0:
#        print(x)
# нужно, чтобы точки лежали и на [23; 37] и на [41; 73] поэтому
# 73 - 23 = 50

# A = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     D = 7 <= x <= 68
#     C = 29 <= x <= 100
#     f = D <= (((not C) and (not A)) <= (not D))
#     if f != f_usl:
#         print(x)
# print(29 - 7)

# A = 1
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = 13 <= x <= 19
#     Q = 17 <= x <= 23
#     f = (not (not P) <= Q) <= (A <= ((not Q) <= P))
#     if f == f_usl:
#         print(x)

# A = 0
# f_usl = 0
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     B = 23 <= x <= 37
#     C = 41 <= x <= 73
#     f = (not(((not B) <= C)) <= A)
#     if f != f_usl:
#         print(x)
#

# A = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = 35 <= x <= 55
#     Q = 45 <= x <= 65
#     f = (P <= A) and ((not A) <= (not Q))
#     if f != f_usl:
#         print(x)


# A = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = 254 <= x <= 800
#     Q = 410 <= x <= 823
#     f = (P and (not A)) <= Q
#     if f != f_usl:
#         print(x)


# A = 0
# f_usl = 0
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = 5 <= x <= 40
#     Q = 41 <= x <= 54
#     R = 6 <= x <= 53
#     f = ((not P) <= Q) and R and (not A)
#     if f != f_usl:
#         print(x)

# A = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = 25 <= x <= 240
#     Q = 175 <= x <= 300
#     R = 270 <= x <= 340
#     f = (Q <= P) or ((not A) <= R)
#     if f != f_usl:
#         print(x)

# A = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = 254 <= x <= 800
#     Q = 410 <= x <= 823
#     f = (P and (not A)) <= Q
#     if f != f_usl:
#         print(x)