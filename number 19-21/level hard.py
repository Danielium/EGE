# def f(s, m, k=''):
#     if s > 40: return m % 2 == 0
#     if m == 0: return 0
#     h = []
#     if k != '+3': h.append(f(s + 3, m - 1, '+3'))
#     if k != '+6': h.append(f(s + 6, m - 1, '+6'))
#     if k != '*2': h.append(f(s * 2, m - 1, '*2'))
#     return any(h) if m % 2 != 0 else all(h)
# print('19', [s for s in range(2, 37) if not f(s, 1) and f(s, 2)])
# print('20', [s for s in range(2, 37) if not f(s, 1) and f(s, 3)])
# print('21', [s for s in range(2, 37) if not f(s, 2) and f(s, 4)])




# def f(s, m, k1='', k2=''):
#     if s >= 29: return m % 2 == 0
#     if m == 0: return 0
#     h = []
#     if k2 != '+1': h.append(f(s + 1, m - 1, '+1', k1))
#     if k2 != '+2': h.append(f(s + 2, m - 1, '+2', k1))
#     if k2 != '*2': h.append(f(s * 2, m - 1, '*2', k1))
#     return any(h) if m % 2 != 0 else all(h)
# print('19', [s for s in range(1, 29) if not f(s, 1) and f(s, 3)])
# print('20', [s for s in range(1, 29) if not f(s, 2) and f(s, 4)])
# print('21', [s for s in range(1, 29) if not f(s, 1) and not f(s, 3) and f(s, 5)])



# def f(s, m):
#     if s <= 12: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s // 3, m - 1), f(s - 12, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
# print('19', [s for s in range(13, 200) if f(s, 2)])
# print('20', [s for s in range(13, 200) if not f(s, 1) and f(s, 3)])
# print('21', len([s for s in range(13, 200) if not f(s, 2) and f(s, 4)]))




# def f(a, b, m, k=0):
#     if a == b: return m % 2 == 0
#     if m == 0: return 0
#     if a > b: h = [f(a, b + 1, m - 1), f(a, b + 3, m - 1)]
#     else: h = [f(a + 1, b, m - 1), f(a + 3, b, m - 1)]
#     if k == 0: return any(h) if m % 2 != 0 else all(h)
#     if k == 1: return any(h) if m % 2 != 0 else sum(h) == 1
# print('19', [s for s in range(1, 24) if not f(13, s, 1) and f(13, s, 2)])
# print('20', [s for s in range(1, 24) if not f(13, s, 1) and f(13, s, 3)])
# print('21', [s for s in range(1, 24) if not f(13, s, 2) and f(13, s, 4) and f(13, s, 2, 1)])



def f(s, m):
    if 50 <= s <= 119: return m % 2 == 0
    if s > 119: return m % 2 != 0
    if m == 0: return 0
    h = [f(s + 2, m - 1), f(s * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)
print('19', len([s for s in range(1, 50) if f(s, 2)]))
print('20', [s for s in range(1, 50) if not f(s, 1) and f(s, 3)])
print('21', [s for s in range(1, 50) if not f(s, 2) and f(s, 4)])

