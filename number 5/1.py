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


# def f(n):
#     d = bin(n)[2:]
#     d += str(d.count('1') % 2)
#     d += str(d.count('1') % 2)
#     return int(d, 2)
# print(min(f(N) for N in range(1,  10000) if f(N) > 80))


# def f(n):
#     b = bin(n)[2:]
#     b += str(b.count('1') % 2)
#     b += str(b.count('1') % 2)
#     return int(b, 2)
# print(min (f(n) for n in range (1, 1000) if f(n) > 75))


# def f(n):
#     b = bin(n)[2:]
#     if b[-1] == '0': b = '10' + bin(n)[2:] + '10'
#     else: b = '1' + bin(n)[2:] + '00'
#     return int(b, 2)
# print(min(f(n) for n in range(1, 100) if f(n) > 100))




# for n in range(28, 200):
#     b = bin(n)[2:]
#     if b.count('1') % 2 == 0:
#         b = '10' + b[2:] + '0'
#     else:
#         b = '11' + b[2:] + '1'
#     r = int(b, 2)
#     print(n, r)


# for x in range(1, 100):
#     b = bin(x)[2:]
#     if b.count('1')%2 == 0:
#         b = b + '0'
#     else: b = b + '1'
#     if b.count('1')%2 == 0:
#         b = b + '0'
#     else: b = b + '1'
#     r = int(b, 2)
#     print(x, r)


# for x in range(1, 100):
#     b = bin(x)[2:]
#     if b.count('1') % 2 == 0:
#         b = b + '01'
#     else: b = b+'10'
#     r = int(b, 2)
#     print(r)


# for x in range(1, 100):
#     b = bin(x)[2:]
#     b = b + b[-1]
#     if b.count('1') % 2 == 0:
#         b = b + '0'
#     else:
#         b = b + '1'
#     if b.count('1') % 2 == 0:
#         b = b + '0'
#     else:
#         b = b + '1'
#     r = int(b, 2)
#     print(x, r)


# for x in range(1000, 10000):
#     s = str(x)
#     a = int(s[0]) * int(s[1])
#     b = int(s[2]) * int(s[3])
#     k = [a, b]
#     n = sorted(k)
#     if n[0] == 12 and n[1] == 14:
#         print(n, x)


# def tr(x):
#     n = ''
#     while x:
#         n = str(x%3)+n
#         x//=3
#     return n




def tr(x):
    n = ''
    while x:
        n = str(x%3)+n
        x//=3
    return n

for n in range(1, 100):
    t = tr(n)
    if (2*t.count('2')+t.count('1'))%2==0:
        t = '12'+t[2:]+'0'
    else: t = '10'+t[2:]+'2'
    r = int(t, 3)
    print(n, r)



