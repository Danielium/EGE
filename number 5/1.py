# def f(N):
#     d = bin(N)[2:]
#     d += str(d.count('1') % 2)
#     d += str(d.count('1') % 2)
#     return int(d, 2)
# print(min(N for N in range(1000) if f(N) > 77))


# def f(N):
#     n = bin(N)[2:]
#     n += str(n.count('1') % 2)
#     n += str(n.count('1') % 2)
#     return int(n, 2)
# print(min(f(N) for N in range(100) if f(N) > 80))


# def f(N):
#     n = bin(N)[2:].zfill(8)
#     n = n.replace('0', '2').replace('1', '0').replace('2', '1')
#     return int(n, 2) + 1
# print(min(N for N in range(128) if f(N) == 221))


# def f(N):
#     r = bin(N)[2:]
#     if int(r) % 2 == 0:
#         r = '10' + r + '10'
#     else:
#         r = '1' + r + '00'
#     return int(r, 2)
# print(min(f(N) for N in range(1, 1000) if f(N) > 100))

# count = 0
# def f(N):
#     d = bin(N)[2:]
#     if d.count('1') % 2 == 0: d = '10' + d
#     else: d = '11' + d
#     if d.count('1') % 2 != 0: d += '11'
#     else: d += '00'
#     return int(d, 2)
# for N in range(1, 1000):
#     if f(N) < 860:
#         count += 1
# print(count)


# def f(N):
#     d = bin(N)[2:]
#     if d.count('1') % 2 == 0:
#         d = '10' + d[2:] + '1'
#     else: d = '11' + d[2:] + '0'
#     return int(d, 2)
# print(max(f(N) for N in range(1, 16)))


# def f(x):
#     r = ''
#     while x > 0:
#         r += str(x % 5)
#         x //= 5
#     return r[::-1]
# def fuck_obzh(N):
#     k = f(N)
#     if int(k[-1]) % 2 == 0: k += '2'
#     else: k = '2' + k + '3'
#     return int(k, 5)
# print(max(N for N in range(1, 100000) if int(fuck_obzh(N) < 1000)))