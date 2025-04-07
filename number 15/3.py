# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = x in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#     Q = x in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
#     A = 1
#     f = (A <= P) and ((not Q) <= (not A))
#     if f != 0:
#         print(x)
# 3 значения ---- 3


# A = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = x in [1, 3, 4, 9, 11, 13, 15, 17, 19, 21]
#     Q = x in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
#     f = (P <= A) or ((not A) <= (not Q))
#     if f != f_usl:
#         print(x)
# print(3 * 9 * 15 * 21)

# A = 1
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     P = x in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#     Q = x in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
#     f = (A <= P) and ((not Q) <= (not A))
#     if f == f_usl:
#         print(x)


# for x in [k * 1/4 for k in range(-10000, 10000)]:
#     P = x in [x for x in range(2, 22, 2)]
#     Q = x in [x for x in range(5, 55, 5)]
#     A = 1
#     f = (A <= P) and (Q <= (not A))
#     if f == 1:
#         print(x)

# def d(m, n):
#     return m%n==0
# def f(x, a):
#     b = x in [x for x in range(60, 81)]
#     return d(x, a) or (b <= (not d(x, 22)))
# print(max(a for a in range(1, 1000) if all(f(x, a) for x in range(1, 1000))))


# def d(n, m):
#     return n%m==0
# def f(a, x):
#     return (d(405, x) <= d(81, x)) or (a - x > 162)
# print(min(a for a in range(1, 1000) if all(f(a, x) for x in range(1, 1000))))


# def f(x, y, a):
#     return (9*x + y > a) or (x>=36) or (y >= 18)
# print(max(a for a in range(1, 500) if all(f(x, y, a) for x in range(1, 500) for y in range(1, 500))))
















