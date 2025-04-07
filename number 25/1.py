# from fnmatch import fnmatch
# for i in range(273, 10**8 + 1, 273):
#     if fnmatch(str(i), '12??15*6'):
#         print(i, i//273)


# from fnmatch import fnmatch
# for i in range(13, 10**8 + 1, 13):
#    if fnmatch(str(i), '123*678'):
#        print(i, i//2)


# from fnmatch import fnmatch
# for i in range(0, 10**10, 2024):
#     if fnmatch(str(i), '1?2157*4'):
#         print(i, i//2024)


# from fnmatch import fnmatch
# for i in range(2023, 10**8, 2023):
#     if fnmatch(str(i), '3?1*57'):
#         print(i, i // 2023)


# from fnmatch import fnmatch
# for i in range(151, 10**9, 151):
#     if fnmatch(str(i), '2?34?56?8'):
#         print(i, i//151)


# from fnmatch import fnmatch
# def sd(x):
#     count = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             count.add(d)
#             count.add(x // d)
#     return sum(count)
#
#
# for i in range(500001, 1000000):
#     if fnmatch(str(sd(i)), '*7?'):
#         print(i, sd(i))


# from fnmatch import fnmatch
# def sc(x):
#     return sum(map(int, str(x)))
# for i in range(2023, 10**9, 2023):
#     if fnmatch(str(i), '20*23') and i % 2023 == 0 and sc(i) % 7 == 0 and sc(i) < 20:
#         print(i)


# from fnmatch import fnmatch
# for i in range(1923, 10**8, 1923):
#     if fnmatch(str(i), '1*2??76'):
#         print(i, i//1923)

# from fnmatch import fnmatch
# def p(x):
#     return all(x > 1 and x % d != 0 for d in range(2, int(x**0.5) + 1))
# for i in range(1, 10**7):
#     if p(i) and fnmatch(str(i), '3?1111*'):
#         print(i)



# from fnmatch import fnmatch
#
# def f(x):
#     c = set()
#     for d in range(1, int(x**0.5)+1):
#         if x % d == 0:
#             if d % 2 == 0:
#                 c.add(d)
#             if (x // d) % 2 == 0:
#                 c.add(x // d)
#     return sorted(c)
#
# for i in range(65000, 1000000):
#     if fnmatch(str(i), '6*97*5?') and len(f(i)) >= 4:
#         print(i, sum(f(i)))



# from fnmatch import fnmatch
# for i in range(237, 10**8, 237):
#     if fnmatch(str(i), '81?2*80') and (not fnmatch(str(i), '*9*')):
#         print(i, i//237)



# from fnmatch import fnmatch
# def f(x):
#     c = set()
#     for d in range(1, int(x**0.5)+1):
#         if x % d == 0:
#             if fnmatch(str(d), '4*'):
#                 c.add(d)
#             if fnmatch(str(x//d), '4*'):
#                 c.add(x // d)
#     return c
# for i in range(1, 10**6):
#     if len(f(i)) == 24:
#         print(i, max(f(i)))


# from fnmatch import fnmatch
# for i in range(28, 10 ** 9, 28):
#     if fnmatch(str(i), '6323*353?'):
#         print(i, i//28)


# from fnmatch import fnmatch
#
# def f(x):
#     return sum(map(int, str(x)))
#
# for i in range(2023, 10**10, 2023):
#     if fnmatch(str(i), '1?1?1?1*1') and f(i) == 22:
#         print(i)



# from fnmatch import fnmatch
# n = 0
# for i in range(4546, 10**10 + 1, 4546):
#     if fnmatch(str(i), '8*80*06'):
#         if n % 60 == 0:
#             print(i, i//4546)
#         n += 1


# from fnmatch import fnmatch
#
# def f(x):
#     c = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             c.add(d)
#             c.add(x // d)
#     return c
# for i in range(1, 10**7 + 1):
#     if fnmatch(str(i), '3*52?'):
#         if len(f(i)) % 2 != 0:
#             f(i).remove(i)
#             print(i, max(f(i)))



# from fnmatch import fnmatch
# def f(x):
#     c = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             c.add(d)
#             c.add(x // d)
#     return c
# for x in range(18, 10 ** 9, 18):
#     if fnmatch(str(x), '*18??18'):
#         if x % 1018 == 0:
#             print(x, len(f(x)))




# def f(x):
#     c = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             c.add(d)
#             c.add(x // d)
#     return c
# for x in range(700001, 701000):
#     k = [a for a in f(x) if a % 10 == 7 and a != x and a != 7]
#     if len(k) > 0:
#         print(x, min(k))

# def div(x):
#     c = set()
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             c.add(i)
#             c.add(x//i)
#     return sorted(c)
# for x in range(550001, 550100):
#     d = [i for i in div(x) if i%10==7]
#     if len(d) == 3:
#         print(x, d[2])



# def prime(x):
#     return x > 1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))
# for x in range(6080068, 6080177):
#     if prime(x): print(x)



# def div(x):
#     c = set()
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             c.add(i)
#             c.add(x//i)
#     return sorted(c)
# for x in range(300000, 300200):
#     d = [i for i in div(x) if i%3==0]
#     if len(d) == 5:
#         print(x, d[4])

# def div(x):
#     c = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             c.add(i)
#             c.add(x//i)
#     return sorted(c)
# for x in range(700_000, 700_200):
#     d = [i for i in div(x) if i%10==7 and i!=7]
#     if len(d)>0:
#         print(x, d[0])


# def div(x):
#     c = set()
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             c.add(i)
#             c.add(x//i)
#     if len(c) == 0: return 0
#     else: return min(c)+max(c)
# for x in range(800_000, 800_200):
#     d = div(x)
#     if d%10==4:
#         print(x, d)


# from fnmatch import fnmatch
# for x in range(0, 10**9, 17):
#     if fnmatch(str(x), '12345?6?8'):
#         print(x, x//17)



# from fnmatch import fnmatch
# for x in range(0, 10**8, 141):
#     if fnmatch(str(x), '1234*7'):
#         print(x, x//141)


# from fnmatch import fnmatch
# for x in range(0, 10**9, 169):
#     if fnmatch(str(x), '123*567?'):
#         print(x, x//169)


# from fnmatch import fnmatch
# for x in range(0, 10**6, 51):
#     if fnmatch(str(x), '12*45*'):
#         print(x, x//51)


# from fnmatch import fnmatch
# for x in range(0, 10**10, 2023):
#     if fnmatch(str(x), '1?2139*4'):
#         print(x, x//2023)



# from fnmatch import fnmatch
# def div(x):
#     c = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             c.add(i)
#             c.add(x//i)
#     return sorted(c)
# for x in range(65000, 660000):
#     if fnmatch(str(x), '6*97*5?'):
#         d = [i for i in div(x) if i%2==0]
#         if len(d) >=4:
#             print(x, sum(d))






























