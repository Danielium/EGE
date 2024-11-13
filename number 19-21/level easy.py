# def f(a, b, m):
#     if a + b >= 342: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(a + 2, b, m-1), f(a, b+2, m-1), f(a*5, b, m-1), f(a, b*5, m-1)]
#     return any(h) if m % 2 != 0 else all(h)
# print('19 - ', [s for s in range(1, 326) if f(11, s, 2)]) # 14
# print('20 - ', [s for s in range(1, 326) if not f(11, s, 1) and f(11, s, 3)]) # 57, 64
# print('21 - ', [s for s in range(1, 326) if not f(11, s, 2) and f(11, s, 4)]) # 65



# def f(s, m):
#     if s >= 273: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 2, m - 1), f(s + 5, m - 1), f(s * 4, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
# print('19', [s for s in range(1, 273) if f(s, 2)]) # 18
# print('20', [s for s in range(1, 273) if not f(s, 1) and f(s, 3)]) # 17, 62
# print('21', [s for s in range(1, 273) if not f(s, 2) and f(s, 4)]) # 60




# def f(s, m):
#     if s >= 281: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 4, m - 1), f(s * 2, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
# print('19 -_-', [s for s in range(1, 281) if not f(s, 1) and f(s, 2)]) # 137
# print('20 -_-', [s for s in range(1, 281) if not f(s, 1) and f(s, 3)]) # 69 70
# print('21 -_-', [s for s in range(1, 281) if not f(s, 2) and f(s, 4)]) # 129




# def f(s, m):
#     if s >= 111: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 1, m - 1), f(s + 3, m - 1), f(s * 4, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
# print('19', [s for s in range(1, 111) if not f(s, 1) and f(s, 2)])
# print('20', [s for s in range(1, 111) if not f(s, 1) and f(s, 3)])
# print('21', [s for s in range(1, 111) if not f(s, 2) and f(s, 4)])




# def f(s, m):
#     if s >= 55: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s + 1, m - 1), f(s + 4, m - 1), f(s * 3, m - 1)]
#     return any(h) if m % 2 != 0 else all(h)
# print('19', [s for s in range(1, 55) if not f(s, 1) and f(s, 2)])
# print('20', [s for s in range(1, 55) if not f(s, 1) and f(s, 3)])
# print('21', [s for s in range(1, 55) if not f(s, 2) and f(s, 4)])




# def f(s, m):
#     if s >= 67: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+1, m-1), f(s+3, m-1), f(s*2, m-1)]
#     return any(h) if m % 2 != 0 else all(h)
# print([s for s in range(1, 67) if not f(s, 1) and f(s, 2)])
# print([s for s in range(1, 67) if not f(s, 1) and f(s, 3)])
# print([s for s in range(1, 67) if not f(s, 2) and f(s, 4)])




# def f(s, m):
#     if s >= 39: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s+1, m-1), f(s+3, m-1), f(s*2, m-1)]
#     return any(h) if m % 2 != 0 else all(h)
# print([s for s in range(1, 39) if not f(s, 1) and f(s, 2)])
# print([s for s in range(1, 39) if not f(s, 1) and f(s, 3)])
# print([s for s in range(1, 39) if not f(s, 2) and f(s, 4)])


# def f(a, b, m):
#     if a + b >= 59: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*2, b, m-1), f(a, b*2, m-1)]
#     return any(h) if m % 2 != 0 else all(h)
# print([b for b in range(1, 53) if not f(5, b, 1) and f(5, b, 2)]) # 14
# print([b for b in range(1, 53) if not f(5, b, 1) and f(5, b, 3)])
# print([b for b in range(1, 53) if not f(5, b, 2) and f(5, b, 4)])



# def f(a, m):
#     if a > 33: return m%2 == 0
#     if m==0: return 0
#     h = [f(a+1, m-1), f(a+2, m-1), f(a+3, m-1), f(a*2, m-1)]
#     return any(h) if m%2!=0 else all(h)
# print([a for a in range(1, 33) if f(a, 2)])
# print([a for a in range(1, 33) if not f(a, 1) and f(a, 3)])
# print([a for a in range(1, 33) if not f(a, 2) and f(a, 4)])


# def f(a, m):
#     if 36 <= a <= 60: return m%2==0
#     if a > 60: return m%2!=0
#     if m==0: return 0
#     h = [f(a+1, m-1), f(a*2, m-1), f(a*3, m-1)]
#     return any(h) if m%2!=0 else all(h)
# print([a for a in range(1, 36) if f(a, 2)])
# print([a for a in range(1, 36) if not f(a, 1) and f(a, 3)])
# print([a for a in range(1, 36) if not f(a, 2) and f(a, 4)])



# def f(a, b, m):
#     if a + b >= 59: return m%2==0
#     if m == 0: return 0
#     h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*2, b, m-1), f(a, b*2, m-1)]
#     return any(h) if m%2!=0 else all(h)
# print([b for b in range(1, 53) if f(5, b, 1)])
# print([b for b in range(1, 53) if not f(5, b, 1) and f(5, b, 3)])
# print([b for b in range(1, 53) if not f(5, b, 2) and f(5, b, 4)])



def f(a, b, m):
    if a + b >= 77: return m%2==0
    if m == 0: return 0
    h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*2, b, m-1), f(a, b*2, m-1)]
    return any(h) if m%2!=0 else all(h)
print([b for b in range(1, 70) if f(7, b, 2)])
print([b for b in range(1, 70) if not f(7, b, 1) and f(7, b, 3)])
print([b for b in range(1, 70) if not f(7, b, 2) and f(7, b, 4)])