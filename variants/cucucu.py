# from itertools import product, permutations
# def f(w, x, y, z):
#     return ((not x) == z) <= (y == (w or x))
# for x1, x2, x3, x4, x5 in product([0, 1], repeat = 5):
#     t = (
#         (0, 0, x1, x2, 0),
#         (0, x3, x4, 0, 0),
#         (0, x5, 0, 0, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('wxyz', r=4):
#             if all(f(**dict(zip(p, l)))==l[-1] for l in t):
#                 print(*p)

# mi = float('inf')
# ma = -float('inf')
# for i in range(1995000000, 2000000000):
#     n = bin(i)[2:]
#     if n.count('1')%2==0: n = '10'+n
#     else: n = '1'+n+'11'
#     r = int(n, 2)
#     mi = min(mi, r)
#     ma = max(ma, r)
# print(mi, ma, mi+ma)
#
# print(549496729+16589934587)


# from turtle import *
# screensize(10000, 10000)
# tracer(0)
# m = 20
# for i in range(6):
#     fd(8*m)
#     rt(120)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*m, y*m)
#         dot(3, 'red')
# update()
# exitonclick()


# c = 0
# for line in open('9cucucu'):
#     u1 = 0
#     u2 = 0
#     u3 = 0
#     x = [int(i) for i in line.split()]
#     if len(x) == len(set(x)): u1+=1
#     if (sum(c for c in x)%2)!=0: u2+=1
#     if (x[1] % (x[0]+x[2])) == 0 or (x[2] % (x[1]+x[3])) == 0 or (x[3] % (x[2]+x[4])) == 0 or (x[4] % (x[3]+x[5])) == 0: u3 += 1
#     if u1 == 0: print(x)
#     if u1+u2+u3 > 0:
#         c+=1
#         print(x, set(x), u1, u2, u3)

#print(c)


# s = 82*'8'
# while '1111' in s or '8888' in s:
#     if '1111' in s: s=s.replace('1111', '8', 1)
#     else: s=s.replace('8888', '11', 1)
# print(s)




# from ipaddress import *
# c = 0
# net = ip_network('192.168.32.160/255.255.255.240', 0)
# for ip in net:
#     print(f'{ip:b}')
#     if f'{ip:b}'.count('1')%2==0:
#         c+=1
# print(c)



from itertools import combinations
def f(x):
    p = 10 <= x <= 50
    q = 30 <= x <= 70
    a = a1 <= x <= a2
    return (not (p <= a)) or q
Ox = [x/4 for x in range(10*4, 70*4)]
m = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) for x in Ox):
        m.append(a2-a1)
print(m)
