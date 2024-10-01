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

for x in range(10, 40):
    if bin(x)[-4:] == '1011':
        print(x)