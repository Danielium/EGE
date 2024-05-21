# def d(n, m):
#     return n % m == 0
# def sb(s, d):
#     return s + d >= 0
# def f(A, x):
#     return (x + A >= 160) or (d(x, 7) <= (not sb(x, -17)))
# print(min(A for A in range(1, 2000) if all(f(A, x) == 1 for x in range(1, 2000))))



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


