# n = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
# count = 0
# while n > 0:
#     if n % 9 != 0: count += 1
#     n //= 9
# print(count)

# n = 361 * 2349 ** 84 - 89 ** 192 + 1953 ** 481 * 4843 ** 151
# count = 0
# while n > 0:
#     if n % 9 == 5: count += 1
#     n //= 9
# print(count)

# n = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
# count = 0
# while n > 0:
#     if n % 25 == 0: count += 1
#     n //= 25
# print(count)

# n = 5**2 * 7**25 + 6**2 * 7**36 - 4**2 * 9**3
# count = 0
# while n > 0:
#     if n % 7 == 0: count += 1
#     n //= 7
# print(count)


# for x in range(1, 2031):
#     count = []
#     n = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
#     while n > 0:
#         count += [n%6]
#         n //= 6
#     if count.count(0) == 202: print(x, count)

# n = 64**30 + 2**300 - 4
# c = []
# while n > 0:
#     c += [n%8]
#     n //= 8
# print(c.count(7))



# n = 3 * 16 ** 8 - 4 ** 5 + 3
# c = []
# while n > 0:
#     c += [n%4]
#     n //= 4
# print(c.count(3))


# n = 2 * 27**7 + 3**10 - 9
# c = []
# while n > 0:
#     c += [n%3]
#     n //= 3
# print(c.count(0))

# n = 51 * 7**12 - 7**3 - 22
# c = []
# while n > 0:
#     c += [n%7]
#     n //= 7
# print(sum(c))


# for x in range(1000):
#     n = 125**200 - 5**x + 74
#     c = []
#     while n > 0:
#         c += [n%5]
#         n //= 5
#     if c.count(4) == 100:
#         print(x)
#         break

# n = 11 * 15**65 + 18*15**38 - 14 * 15**17 + 19 * 15**11 + 18338
# c = []
# while n > 0:
#     c += [n%15]
#     n //= 15
# print(len(set(c)))

# for x in range(1, 20):
#     if int('33', x+4) - int('33', 4) == 33:
#         print(x)


# for x in range(2, 40):
#     try:
#         if int('103', x) == int('97', x + 2):
#             print(x)
#     except:
#         ...

# for x in range(10, 40):
#     if bin(x)[-4:] == '1011':
#         print(x)

# n = 3 * 3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
# c = []
# while n>0:
#     c+=[n%25]
#     n//=25
# print(c)


# n = 6*144**26 + 11*12**75-48
# c = []
# while n>0:
#     c+=[n%12]
#     n//=12
# print(c.count(11))


# for x in range(30):
#     n = 36**17 - 6**x + 71
#     c = []
#     while n>0:
#         c+=[n%6]
#         n//=6
#     if sum(c) == 61:
#         print(x)

# n = 5*216**1156 - 4*36**1147 + 6**1153 - 875
# c=[]
# while n>0:
#     c+=[n%6]
#     n//=6
# print(c.count(5)-c.count(0))



# for n in range(2, 20):
#     try:
#         if int('132', n) + int('13', 8) == int('124', n+1):
#             print(n)
#     except:
#         ...


# for n in range(2, 20):
#     try:
#         if int('21', n) * int('13', n) == int('313', n):
#             print(n)
#     except: ...


# def f(x, cc):
#     a = []
#     while x>0:
#         a += [x%cc]
#         x//=cc
#     return a
# count = 0
# for x in range(1000):
#     if len(f(x, 5)) <= 4 and len(f(x, 2)) >= 5 and x%16 == 13:
#         count += 1
# print(count)



# for x in range(15):
#     print((int(f'123{x}5', 15) + int(f'1{x}233', 15))/14)



# n = 5*729**2024 + 3*243**1413 - 7*81**169 - 2*9**107 + 3017
# c = []
# while n > 0:
#     c+=[n%27]
#     n//=27
# print(sum(i for i in c if i<=25 and i%2==0))