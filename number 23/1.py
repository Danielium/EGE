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


# def f(x, end):
#     if x < end: return 0
#     if x == end: return 1
#     return f(x - 2, end) + f(x // 2, end)
# print(f(38, 10) * f(10, 2))

# def f(x, end):
#     if x > end: return 0
#     if x==end: return 1
#     return f(x+1, end) + f(x+3, end) + f(x*2, end)
# print(f(1, 15))

# def f(x, end):
#     if x > end: return 0
#     if x==end: return 1
#     return f(x+1, end) + f(x*2, end) + f(x**2, end)
# print(f(5, 154))


# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x+1, end) + f(x+2, end) + f(x*4, end)
# print(f(1, 13))

# def f(x, end):
#     if x < end: return 0
#     if x==end: return 1
#     return f(x-2, end) + f(x-5, end)
# print(f(23, 2))


# def f(x, end):
#     if x < end: return 0
#     if x==end: return 1
#     return f(x-1, end) + f(x-3, end) + f(x//3, end)
# print(f(22, 2))


# def f(x, end):
#     if x > end: return 0
#     if x==end: return 1
#     return f(x+1, end) + f(x*2, end)
# print(f(1, 10) * f(10, 20))



# def f(x, end, c):
#     if x%2==0: c+=1
#     if x>end:return 0
#     if x==end:return c==6
#     return f(x+1, end, c) + f(x+3, end, c) + f(x+5, end, c)
# print(f(3, 25, 0))



# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x+1, end)+f(x+3, end)+f(x * 2,  end)
# print(f(3, 9)*f(9, 12)*f(12, 20))


# def f(x, end):
#     if x>end: return 0
#     if x==end: return 1
#     return f(x+1, end) + f(x*2, end)
# print(f(1, 12)*f(12, 30))



# def f(x, end):
#     if x==end: return 1
#     if x<end: return 0
#     return f(x-8, end)+f(x//2, end)
# print(f(102, 43)*f(43, 5))


# def f(x, end):
#     if x == end: return 1
#     if x>end or x==6: return 0
#     return f(x+2, end) + f(x*3, end)
# print(f(1, 25)*f(25, 63))



# def f(x, end):
#     if x == end: return 1
#     if x>end or x==11 or x==18: return 0
#     return f(x+1, end)+f(x+2, end)+f(x*3, end)
# print(f(4, 8)*f(8, 23))


# def f(x, end):
#     if x == end: return 1
#     if x > end: return 0
#     return f(x+1, end)+f(x*2, end)+f(x*2+1, end)+f(x*10, end)
# print(f(1, 15))









