# a = [int(x) for x in open('1')]
# c = []
# m = max(n for n in a if abs(n) % 100 == 15)
# for i in range(len(a) - 2):
#     if ((1000 <= abs(a[i]) <= 9999) + (1000 <= abs(a[i+1]) <= 9999) + (1000 <= abs(a[i+2]) <= 9999)) == 1:
#         if (a[i] + a[i+1] + a[i+2]) >= m:
#             c.append(a[i] + a[i+1] + a[i+2])
#
# print(len(c), max(c))


# a = [int(x) for x in open('2')]
# m = max(abs(n) for n in a if n % 1001 == 0)
# c = []
# for i in range(len(a)-1):
#     if (100 <= abs(a[i]) <= 999) + (100 <= abs(a[i+1]) <= 999) == 1:
#         if (a[i]) + (a[i+1]) > m:
#             c.append(a[i] + a[i+1])
# print(len(c), min(c))


# a = [int(x) for x in open('3')]
# c = []
# m = min(abs(n) for n in a if n % 10 == 3 and 100 <= n <= 999)
# for i in range(len(a) - 1):
#     if (1000 <= abs(a[i]) <= 9999) + (1000 <= abs(a[i+1]) <= 9999) == 1:
#         if (a[i]**2 + a[i+1]**2) % m == 0:
#             c.append(a[i]**2 + a[i+1]**2)
# print(len(c), max(c))


# a = [int(x) for x in open('4')]
# c = []
# m = min(abs(n) for n in a if n % 10 == 5 and 100 <= abs(n) <= 999)
# for i in range(len(a) - 1):
#     if (100 <= a[i] <= 999) or (100 <= a[i+1] <= 999):
#         if (a[i] + a[i + 1]) % m == 0:
#             c.append(a[i] + a[i + 1])
# print(len(c), max(c))


# a = [int(x) for x in open('5')]
# m = min(abs(n) for n in a)
# c = []
# for i in range(len(a) - 1):
#     if (a[i] % 117 == m) or (a[i+1] % 117 == m):
#         c.append(a[i] + a[i+1])
# print(len(c), max(c))


#  a = [int(x) for x in open('6')]
#  m = max(n for n in a if abs(n) % 100 == 54)
#  c = []
#  for i in range(len(a) - 1):
#      if abs(a[i])%10 == abs(a[i+1]) % 10:
#          if abs(a[i]) + abs(a[i+1]) <= m:
#              c.append(max(a[i], a[i+1]))
#  print(len(c), max(c))


# def f(x):
#     return x > 1 and all(x % d != 0 for d in range(2, int(x**0.5) + 1))
# a = [int(x) for x in open('7')]
# m = max(n for n in a if abs(n) % 100 == 17)
# c = []
# for i in range(len(a) - 1):
#     if f(a[i]) + f(a[i+1]) == 1:
#         if (a[i] + a[i+1]) % m == 0:
#             c.append(a[i] * a[i+1])
#
# print(len(c), max(c))


# a = [int(x) for x in open('8')]
# m = max(abs(n) for n in a if 10 <= abs(n) <= 99)
# c = []
# for i in range(len(a) - 1):
#     if (10 <= abs(a[i]) <= 99) + (10 <= abs(a[i+1]) <= 99):
#         if (a[i] + a[i+1]) % m == 0:
#             c.append(a[i] + a[i+1])
# print(len(c), max(c))



# a = [int(x) for x in open('9')]
# m = min(a)
# c = []
# for i in range(len(a) - 1):
#     if abs(a[i]) % 111 == m or abs(a[i+1]) % 111 == m:
#         c.append(a[i] + a[i+1])
# print(len(c), min(c))


# a = [int(x) for x in open('10')]
# m = max(n for n in a if abs(n) % 10 == 3)
# c = []
# for i in range(len(a) - 1):
#     if (abs(a[i]) % 10 == 3) + (abs(a[i+1]) % 10 == 3) == 1:
#         if a[i] ** 2 + a[i+1] ** 2 >= m ** 2:
#             c.append(a[i] ** 2 + a[i+1] ** 2)
# print(len(c), max(c))


# a = [int(x) for x in open('1')]
# m = min(x for x in a if 100 <= x <= 999 and x % 10 == 3)
# p = []
# for i in range(len(a) - 1):
#     if (1000 <= a[i] <= 9999) + (1000 <= a[i+1] <= 9999) == 1:
#         if (a[i]**2 + a[i+1]**2) % m == 0:
#             p.append(a[i]**2 + a[i+1]**2)
# print(len(p), max(p))

# a = [int(x) for x in open('1')]
# m = max(x for x in a if 10 <= x <= 99)
# p = []
#
# for i in range(len(a) - 1):
#     if (10 <= a[i] <= 99) + (10 <= a[i+1] <= 99) == 1:
#         if (a[i] + a[i+1]) % m == 0:
#             p.append(a[i] + a[i+1])
# print(len(p), max(p))


# a = [int(x) for x in open('1')]
# m = min(x for x in a if x>0 and x%41 == 0)
# p = []
# for i in range(len(a) - 1):
#     if (a[i] != a[i+1]) and (abs(a[i] - a[i+1]) % m == 0):
#         p.append(a[i] + a[i+1])
# print(len(p), max(p))



# a = [int(x) for x in open('1')]
# c=[]
# for i in range(len(a)-1):
#     if abs(a[i]+a[i+1]) % 3 == 0 and abs(a[i]+a[i+1]) %6!=0 and abs(a[i] * a[i+1])%10==8:
#         c.append(a[i]+a[i+1])
# print(len(c), max(c))


# a = [int(x) for x in open('1')]
# c = []
# for i in range(len(a)-3):
#     if (a[i] > a[i+1] > a[i+2] > a[i+3]) and (a[i] - a[i+3])>1000:
#         c.append(a[i] + a[i+1] + a[i+2] + a[i+3])
# print(len(c), min(c))



# a = [int(x) for x in open('1')]
# ma = max(a)
# mi = min(a)
# c = []
# for i in range(len(a)-1):
#     if (a[i] % 3 == ma % 3) + (a[i+1] % 3 == ma % 3) >= 1:
#         if (a[i] % 7 == mi % 7) + (a[i+1] % 7 == mi % 7) >= 1:
#             c.append(a[i]+a[i+1])
# print(len(c), max(c))



























