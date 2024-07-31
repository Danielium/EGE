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


for x in range(1, 2031):
    count = []
    n = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    while n > 0:
        count += [n%6]
        n //= 6
    if count.count(0) == 202: print(x, count)