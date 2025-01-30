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


for x in [k * 1/4 for k in range(-10000, 10000)]:
    P = x in [x for x in range(2, 22, 2)]
    Q = x in [x for x in range(5, 55, 5)]
    A = 1
    f = (A <= P) and (Q <= (not A))
    if f == 1:
        print(x)
















