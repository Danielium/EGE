# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x + 4, end) + f(x * 2, end)
# print(f(13, 42))

# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x + 3, end) + f(x + 4, end) + f(x + 2, end)
# print(f(6, 32) * f(32, 35) * f(35, 44))


# def f(x, end):
#     if x < end: return 0
#     if x == end: return 1
#     return f(x - 3, end) + f(x // 2, end) + f(x - 5, end)
# print(f(43, 32) * f(32, 16))


# def f(x, end):
#     if x < end or x == 35: return 0
#     if x == end: return 1
#     return(f(x // 3, end) + f(x - 2, end) + f(x - 5, end))
# print(f(41, 37) * f(37, 8))


# def f(x, end):
#     if x > end or x == 32: return 0
#     if x == end: return 1
#     return f(x + 2, end) + f(x + 4, end)
# print(f(9, 27) * f(27, 29) * f(29, 37))


# def f(x, end):
#     if x > end or x == 15: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x + 2, end) + f(x * 3, end)
# print(f(6, 21) * f(21, 25))
# print(1320 + 1380)


# def f(x, end):
#     if x > end or x == 43: return 0
#     if x == end: return 1
#     return f(x + 2, end) + f(x + (x + 1), end) + f(x + (x - 1), end)
# print(f(7, 63))



# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x+1, end) + f(x*2, end)
# print(f(2, 7) * f(7, 16) * f(16, 39))


def f(x, end):
    if x < end: return 0
    if x == end: return 1
    return f(x - 2, end) + f(x // 2, end)
print(f(38, 10) * f(10, 2))