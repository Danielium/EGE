# def d(n, m):
#     return n % m == 0
# def sb(s, d):
#     return s + d >= 0
# def f(A, x):
#     return (x + A >= 160) or (d(x, 7) <= (not sb(x, -17)))
# print(min(A for A in range(1, 2000) if all(f(A, x) == 1 for x in range(1, 2000))))
from binascii import a2b_qp
# def d(n, m):
#     return n % m == 0
# def f(A, x):
#     return (d(x, 3) <= (not d(x, 2))) or (x - A >= 4)
# print(max(A for A in range(1, 1000) if all(f(A, x) == 1 for x in range(1, 1000))))



#def d(n, m):
#  return n % m == 0
#def f(x, A):
#    return (d(A, 12) and (d(530,x) <= ((not d(A, x)) <= (not(d(170, x))))))
#print(max(A for A in range(1, 1000) if all(f(x, A) == 1 for x in range(1, 1000))))


# def d(n, m):
#     return n % m == 0
# def f(x, A):
#     return d(x, A) or ((70 <= x <= 90) <= (not d(x, 22)))
# print(max(A for A in range(1, 1000) if all(f(x, A) == 1 for x in range(1, 2000))))

# def f(x):
#     return ((x%a==0) and (x%24==0) and (not x%16==0)) <= (not x%a==0)
# for a in range(1, 20000):
#     if all(f(x) for x in range(1, 200000)):
#         print(a)
#         break




# def f(x):
#     return ((x%84!=0) or (x%90!=0)) <= (x%a!=0)
# for a in range(1, 3000):
#     if all(f(x)for x in range(1, 30000)):
#         print(a)
#         break

# def f(x):
#     return ((x%15==0) and (x%21!=0)) <= ((x%a!=0) or (x%15!=0))
# for a in range(1, 5000):
#     if all(f(x) for x in range(1, 5000)):
#         print(a)

# def f(x):
#     return ((x%4!=3) or (x%6!=1)) <= (x%36!=a)
# for a in range(1, 1000):
#     if all(f(x) for x in range(1, 1000)):
#         print(a)


# def f(x):
#     return (((x&13!=0) or (x&a!=0)) <= (x&13!=0)) or ((x&a!=0) and (x&39==0))
# for a in range(1, 10000):
#     if all(f(x) for x in range(1, 10000)):
#         print(a)


# def f(x, y):
#     return (x>39) or (y>26) or (2*x+4*y<a)
# for a in range(1,1000):
#     if all(f(x,y) for x in range(1, 1000) for y in range(1, 1000)):
#         print(a)
#         break

# a = set(range(1000))
# def f(x):
#     A = x in a
#     P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
#     Q = x in {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
#     return (A <= P) and (Q <= (not A))
# for x in range(1000):
#     if f(x) == 0:
#         a.remove(x)
# print(a)


# from itertools import *
#
# def f(x):
#     P = 25 <= x <= 50
#     Q = 54 <= x <= 75
#     A = a1 <= x <= a2
#     return Q <= ((P==Q) or ((not P)<=A))
#
# ox = [i/4 for i in range(24*4, 76*4+1)]
# m = []
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         m.append(a2-a1)
# print(min(m))



# from itertools import combinations
# def f(x):
#     D = 17 <= x <= 58
#     C = 29 <= x <= 80
#     A = a1 <= x <= a2
#     return D <= (((not C) and (not A)) <= (not D))
# ox = [i/4 for i in range(17*4, 80*4+1)]
# n = []
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         n.append(a2-a1)
# print(min(n))



# from itertools import combinations
# def f(x):
#     P = 17<=x<=54
#     Q = 37<=x<=83
#     A = a1<=x<=a2
#     return P <= ((Q and (not A)) <= (not P))
# ox = [x/4 for x in range(17*4, 83*4)]
# n = []
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         n.append(a2-a1)
# print(min(n))




# from itertools import combinations
# def f(x):
#     P = 15<=x<=40
#     Q = 21<=x<=63
#     A = a1<=x<=a2
#     return P <= ((Q and (not A)) <= (not P))
# ox = [i * 0.25 for i in range(15*4, 63*4)]
# m = []
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#      m.append(a2-a1)
# print(min(m))


# def f(x, y):
#     return (x<=19) or (y < 2*x + a - 50) or (y>17)
# for a in range(1000):
#     if all(f(x, y) for x in range(2000) for y in range(2000)):
#         print(a)
#         break


# def f(x, y):
#     return (x+y <= 30) or (y <= x+2) or (y>=a)
# for a in range(500):
#     if all(f(x, y) for x in range(500) for y in range(500)):
#         print(a)



# def f(x):
#     B = 70<=x<=90
#     return (x%a==0) or (B<=(x%22!=0))
# for a in range(1,500):
#     if all(f(x) for x in range(1,500)):
#         print(a)


# from itertools import combinations
# def f(x):
#     P = 15<=x<=40
#     Q = 21<=x<=63
#     A = a1<=x<=a2
#     return P <= ((Q and (not A)) <= (not P))
# ox = [x*0.25 for x in range(15*4, 63*4)]
# m = []
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         m.append(a2-a1)
# print(min(m))



# from itertools import combinations
# def f(x):
#     B = 24<=x<=90
#     C = 47<=x<=115
#     A = a1<=x<=a2
#     return C <= (((not A) and B) <= (not C))
# ox = [x * 0.25 for x in range(24*4, 115*4)]
# m = []
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         m.append(a2-a1)
# print(min(m))



# from itertools import combinations
# def f(x):
#     b = 18 <= x <= 52
#     c = 16 <= x <= 41
#     a = a1 <= x <= a2
#     return (b <= a) and ((not c) or a)
# Ox = [1/4*x for x in range(16*4, 52*4)]
# m = []
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) for x in Ox):
#         m.append(a2-a1)
# print(max(m))


# from itertools import combinations
# def f(x):
#     m = 32 <= x <= 68
#     n = 54 <= x <= 76
#     a = a1 <= x <= a2
#     return (not (m or n)) == (not a)
# Ox = [x/4 for x in range(32*4, 76*4)]
# m = []
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) for x in Ox):
#         m.append(a2-a1)
# print(m)




# from itertools import combinations
# def f(x):
#     m = 32 <= x <= 68
#     n = 54 <= x <= 76
#     a = a1 <= x <= a2
#     return (not(m or n)) == (not a)
# ox = [x/4 for x in range(32*4, 76*4)]
# m = []
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         m.append(a2-a1)
# print(min(m))




# from itertools import combinations
# def f(x):
#     b = 24 <= x <= 90
#     c = 47 <= x <= 115
#     a = a1 <= x <= a2
#     return (c) <= (((not a) and (b)) <= (not c))
# ox = [x/4 for x in range(24*4, 115*4)]
# m = []
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         m.append(a2-a1)
# print(min(m))




# from itertools import combinations
# def f(x):
#     p = 25 <= x <= 73
#     q = 75 <= x <= 118
#     a = a1 <= x <= a2
#     return ((a) and (not q)) <= ((p) or (q))
# m = []
# ox = [x/4 for x in range(25*4, 118*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         m.append(a2-a1)
# print(max(m))










