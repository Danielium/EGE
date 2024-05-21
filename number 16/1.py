# def f(n):
#     if n == 1: return 1
#     if n % 2 == 0: return n + f(n-1)
#     if n % 2 != 0 and n > 1: return 2 * f(n-2)
# print(f(26))

#  def f(n):
#      if n == 0: return 1
#      if n == 1: return 3
#      if n == 2: return 2
#      if n > 2: return f(n-1) * f(n-3)
#
#  print(f(7))


# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n <= 3: return 1
#     if n > 3: return (n + 3) * f(n - 2)
# for i in range(1, 2050):
#     f(i)
# print(f(2028)/(f(2024)))


# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n < 3: return 2 ** 1024
#     if n > 2: return 2 * n + 3 + f(n-2)
# for n in range(1, 4080):
#     f(n)
# print(f(4048) - f(16))

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n < 3: return 2
#     if n > 2: return 2 * f(n - 2)
# for n in range(1, 2300):
#     f(n)
# print(f(2222) / f(2182))

# def g(n):
#     if n > 100: return n
#     if n <= 100: return g(n+2) + 1
# def f(n):
#     if n <= 1: return n
#     if n > 1 and n % 3 == 0: return f(n-1) + f(n-2) + 1
#     if n > 1 and n % 3 != 0: return g(n-3)
#
# print(f(15) + f(12))

#from functools import lru_cache
#count = 0
#@lru_cache(None)
#def f(n):
#    if n == 0: return 0
#    if n > 0 and n%2==0: return f(n/2) - 1
#    if n > 0 and n%2!=0: return 1 + f(n-1)
#for n in range(1000):
#    if f(n) == 0:
#        count += 1
#print(count)

# count = 0
# def f(n):
#     if n == 0: return 0
#     if n > 0 and n % 2 == 0: return f(n/2)
#     if n % 2 != 0: return 1 + f(n - 1)
# for n in range(1, 501):
#     if f(n) == 8:
#         count+=1
# print(count)

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n < 11: return n
#     if n >= 11: return n + f(n-1)
# for n in range(1, 2100):
#     f(n)
# print(f(2024) - f(2021))

def f(n):
    if n == 1: return 1
    if n > 1 and n % 2 != 0: return 3 * n + f(n-2)
    if n > 1 and n % 2 == 0: return 4 * f(n/2)
print(f(42))