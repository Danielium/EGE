#1
# from fnmatch import fnmatch
# for i in range(0, 10**8, 2023):
#     if fnmatch(str(i), '3?1*57'):
#         print(i, i//2023)

#2
# from fnmatch import fnmatch
# for i in range(0, 10**9, 151):
#     if fnmatch(str(i), '2?34?56?8'):
#         print(i, i//151)


#3
# def sd(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             d.add(i)
#             d.add(x//i)
#     return sum(d)
# from fnmatch import fnmatch
# for i in range(500000, 500500):
#     if fnmatch(str(sd(i)), '*7?'):
#         print(i, sd(i))


#4
# from fnmatch import fnmatch
# def sc(x):
#     return sum((int(c) for c in str(x)))
# for i in range(0, 10**9, 2023):
#     if fnmatch(str(i), '20*23'):
#         if sc(i)%7 == 0 and sc(i) < 20:
#             print(i)


#5
# from fnmatch import fnmatch
# for i in range(0, 10**8, 253):
#     if fnmatch(str(i), '12??15*6'):
#         print(i, i//253)



#6
# from fnmatch import fnmatch
# for i in range(0, 10**8, 1923):
#     if fnmatch(str(i), '1*2??76'):
#         print(i,i//1923)


#7
# from fnmatch import fnmatch
# def p(x):
#     return x>1 and all(x % d != 0 for d in range(2, int(x**0.5)+1))
# for i in range(0, 10**7):
#     if fnmatch(str(i), '3?1111*') and p(i):
#         print(i)


#8
# from fnmatch import fnmatch
# def d(x):
#     delit = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             if i%2==0:
#                 delit.add(i)
#             if (x//i)%2==0:
#                 delit.add(x//i)
#     return delit
# for i in range(65000, 2000000):
#     if fnmatch(str(i), '6*97*5?') and len(d(i))>3:
#         print(i, sum(d(i)))




#9
# from fnmatch import fnmatch
# for i in range(0, 10**8, 237):
#     if fnmatch (str(i), '81?2*80') and not fnmatch (str(i), '*9*'):
#         print(i, i//237)


#10
# from fnmatch import fnmatch
# def f(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             if fnmatch(str(i), '4*'):
#                 d.add(i)
#             if fnmatch(str(x//i), '4*'):
#                 d.add(x//i)
#     return d
# for i in range(10**6):
#     if len(f(i))==24:
#         print(i, max(f(i)))


#11
# from fnmatch import fnmatch
# for i in range(0, 10**9, 28):
#     if fnmatch(str(i), '6323*353?'):
#         print(i, i//28)


#12
# from fnmatch import fnmatch
# def f(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             if i%2==0:
#                 d.add(i)
#             if (x//i)%2==0:
#                 d.add(x//i)
#     return d
# for i in range(65000, 1000000):
#     if fnmatch(str(i), '6*97*5?'):
#         if len(f(i)) > 3:
#             print(i, sum(f(i)))



#13
# from fnmatch import fnmatch
# for i in range(0, 10**8, 1923):
#     if fnmatch(str(i), '1*2??76'):
#         print(i, i//1923)


#14
# from fnmatch import fnmatch
# count = 0
# for i in range(0, 10**10 + 1, 4546):
#     if fnmatch(str(i), '8*80*06'):
#         if count%60 == 0:
#             print(i, i//4546)
#         count += 1


#15
# from fnmatch import fnmatch
# def p(x):
#     return x>1 and all(x%d!=0 for d in range(2, int(x**0.5)+1))
# def pr(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             if p(i): d.add(i)
#             if p(x//i): d.add(x//i)
#     return d
# def e(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             if i%2==0: d.add(i)
#             if (x//i)%2==0: d.add(x//i)
#     return d
# def m(x):
#     return abs(sum(pr(x))-sum(e(x)))
# for i in range(100_000_000, 100_100_000):
#     if len(pr(i)) == len(e(i)):
#         print(i, m(i))



#16
# from fnmatch import fnmatch
# def sc(x):
#     return sum(int(i) for i in str(x))
# for i in range(2023, 10**9, 2023):
#     if fnmatch(str(i), '20*23'):
#         if sc(i)%7==0 and sc(i) < 20:
#             print(i)



#17
# from fnmatch import fnmatch
# for i in range(253, 10**8, 253):
#     if fnmatch(str(i), '12??15*6'):
#         print(i, i//253)

#18
# from fnmatch import fnmatch
# def f(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             if fnmatch(str(i), '4*'):
#                 d.add(i)
#             if fnmatch(str(x//i), '4*'):
#                 d.add(x//i)
#     return d
# for i in range(10**6):
#     if len(f(i))==24:
#         print(i, max(f(i)))



#19
# from fnmatch import fnmatch
# def sc(x):
#     return sum(int(i) for i in str(x))
# def f(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             d.add(i)
#             d.add(x//i)
#     return d
# for i in range(53, 10**7, 53):
#     if fnmatch(str(i), '*2?2*'):
#         if str(i) == str(i)[::-1]:
#             if len(f(i))>30:
#                 print(i, sum(f(i)))


#20
# from fnmatch import fnmatch
# def f(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             d.add(i)
#             d.add(x//i)
#     return d
# for i in range(int((10**9)**0.5)+1):
#     x = i**2
#     if fnmatch(str(x), '15*3*09'):
#         D = sorted(f(x))
#         if len(D)==9:
#             print(x, D[-2])

#21
# from fnmatch import fnmatch
# def d(x):
#     delit = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             if i%2==0:
#                 delit.add(i)
#             if (x//i)%2==0:
#                 delit.add(x//i)
#     return delit
# for i in range(65000, 2000000):
#     if fnmatch(str(i), '6*97*5?') and len(d(i))>3:
#         print(i, sum(d(i)))

#22
# from fnmatch import fnmatch
# def p(x):
#     return x>1 and all(x % d != 0 for d in range(2, int(x**0.5)+1))
# for i in range(0, 10**7):
#     if fnmatch(str(i), '3?1111*') and p(i):
#         print(i)

#23
# from fnmatch import fnmatch
# for i in range(141, 10**8, 141):
#     if fnmatch(str(i), '1234*7'):
#         print(i, i//141)

#24
# from fnmatch import fnmatch
# def f(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             d.add(i)
#             d.add(x//i)
#     return d
# for i in range(int((10**7)**0.5 + 1)):
#     x = i**2
#     if fnmatch(str(x), '3*52?'):
#         D = sorted(f(x))
#         print(x, D[-2])


#25
from fnmatch import fnmatch
for i in range(2024, 10**10, 2024):
    if fnmatch(str(i), '1?2157*4'):
        print(i, i//2024)













