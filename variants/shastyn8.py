#9
# c=0
# k = 0
# for line in open('9shastyn'):
#     c += 1
#     n = sorted([int(x) for x in line.split()])
#     if len(n) == len(set(n)):
#         if (n[0] + n[-1])**2 > n[1]**3 + n[2]**3:
#             k += c
# print(k)

#13
# from ipaddress import *
# net = ip_network('158.214.121.40/255.255.255.224', 0)
# for ip in net:
#     print(ip)

#14
# n = 5*729**2024 + 3*243**1413 - 7 * 81**169 - 2*9**107 + 3017
# c = []
# while n > 0:
#     c += [n%27]
#     n//=27
# print(sum(x for x in c if x%2==0 and x<=25))


#15
# def d(n, m):
#     return n % m == 0
# def f(a, x):
#     b = 170 <= x <= 220
#     return d(x, a) or (b <= (not d(x, 24)))
# print(len(list((a for a in range(1, 1000) if all(f(a, x) for x in range(1, 1000))))))


#16
# from functools import lru_cache
# def f(n):
#     if n < 15: return 4
#     if n >= 15 and n%3==0: return f(2*n/3) + n - 1
#     if n >=15 and n%3!=0: return f(n-1)+3
# for n in range(1, 200):
#     if int(f(n)) == 251:
#         print(n)


#17
# f = open('17shastyn8')
# n = [int(x) for x in f]
# s = len([x for x in n if x%10==7])
# c = []
# for i in range(len(n)-1):
#     if (n[i] * n[i+1]) < 0:
#         if (n[i] + n[i+1]) < s:
#             c.append(n[i] + n[i+1])
# print(len(c), max(c))

#19-21
# def f(a, b, m):
#     if a + b <= 100: return m%2==0
#     if m==0: return 0
#     h = [f(a-3, b-3, m-1), f(a//2, b, m-1), f(a, b//2, m-1)]
#     return any(h) if m%2!=0 else all(h)
# print('19', [s for s in range(53, 200) if f(48, s, 2)])
# print('20', [s for s in range(53, 2000) if (not f(48, s, 1)) and f(48, s, 3)])
# print('21', [s for s in range(53, 2000) if (not f(48, s, 2)) and f(48, s, 4)])

#23
# def f(a,b, count_):
#     if a == 20:
#         count_ -= 1
#     if a == 30:
#         count_ -= 1
#     if a == b:
#         return 1
#     if a > b or (a == 30 and count_ == 0):
#         return 0
#     else:
#         return f(a + 2, b,count_) + f(a + 3, b,count_) + f(a*2, b,count_)
# print(f(8, 35,2))



#25
# from fnmatch import fnmatch
# for i in range(0, 10**10, 1984):
#     if fnmatch(str(i), '[2468]9?23?*23[13579][02468]'):
#                 print(i, i//1984)





