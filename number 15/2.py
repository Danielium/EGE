#def f(x, y, A):
#    return (3 * x + y > 48) or (x > y) or (4 * x + y < A)
#print(max(A for A in range(0, 100) if any(f(x, y, A) == 0 for x in range(0, 100) for y in range(0, 100))))
# 60

#def f(x, y, A):
#    return (x**2 + y**2 > 1024 - x) or (y < -2 * x + A)
#print(min(A for A in range(200) if all(f(x, y, A) for x in range(200) for y in range(200))))
# 71

# def f(x, a):
#     return (a + x > 700 - a) and ((a%100) + (100%x) > 50)
# print(min(a for a in range (1, 1000) if all(f(x, a) == 1 for x in range(1, 1000))))
# 351


# def f(x, y, a):
#     return (x+2*y < a) or (y > x) or (x > 60)
# print(min(a for a in range(1000) if all(f(x, y, a) == 1 for x in range(100) for y in range(100))))



# def f(A, x):
#     return (x & 29 == 0) or ((x & 11 == 0) <= (not(x & A == 0)))
# print(min(A for A in range(1, 2000) if all(f(A, x) == 1 for x in range(15, 31))))



# def f(A, x, y):
#     return ((x + 2 * y) != 58) or (((A - x) > 0) == ((A + y) > 0))
# print(min(A for A in range(1, 700) if all(f(A, x, y) == 1 for x in range(1, 700) for y in range(1, 700))))



# def f(x, y, A):
#     return (x + y <= 32) or (y <= x + 4) or (y >= A)
# print(max(A for A in range(0, 1000) if all(f(x, y, A) == 1 for x in range(1, 1000) for y in range(1, 1000))))


# def f(x, A):
#     return ((x & 103 == 0) and ((x & 94) != 0)) <= ((x & A) != 0)
# print(min(A for A in range(1, 1000) if all(f(x, A) == 1 for x in range(1, 1000))))


# def f(x, A):
#     return ((x & 52 != 0) and (x & 36 == 0)) <= (not x & A == 0)
# print(min(A for A in range(0, 1000) if all(f(x, A) == 1 for x in range(0, 1000))))


# def f(x, y, A):
#     return (x >= 9) or (2 * x < y) or (x * y < A)
# print(min(A for A in range(500) if all(f(x, y, A) == 1 for x in range(500) for y in range(500))))


# def f(x, A):
#     return ((x & 17 != 0) <= ((x & A != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & A != 0) and (x & 58 == 0))
# print(min(A for A in range(1, 1000) if all(f(x, A) == 0 for x in range(1, 1000))))


# def f(x, y, A):
#     return (x * y < A) or (x < y) or (9 < x)
# print(min(A for A in range(500) if all(f(x, y, A) == 1 for x in range(500) for y in range(500))))



# def f(x, y, A):
#     return (x + 2 * y < A) or (y > x) or (x > 60)
# print(min(A for A in range(500) if all(f(x, y, A) == 1 for x in range(500) for y in range(500))))


def f(x, y, A):
    return ((x + y) <= 24) or (y <= (x - 2)) or (y >= A)
print(max(A for A in range(1, 500) if all(f(x, y, A) == 1 for x in range(1, 500) for y in range(1, 500))))