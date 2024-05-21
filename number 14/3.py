# for x in range(29):
#     x1 = sum(c * 29 ** i for i, c in enumerate([4, 7, x, 4, 2, 6, 9, 6][::-1]))
#     x2 = sum(c * 29 ** i for i, c in enumerate([8, x, 2, 2][::-1]))
#     if (x1 + x2) % 28 == 0: print(x, (x1 + x2) / 28)

#for x in range(27):
#    x1 = sum(c * 27 ** i for i, c in enumerate([1, 7, x, 3, 5][::-1]))
#    x2 = sum(c * 27 ** i for i, c in enumerate([x, 7, 4, 2, int('m', 27)][::-1]))
#    x3 = x ** 3
#    if (x1 + x2 + x3) % 23 == 0: print(x, (x1 + x2 + x3) / 23)



#LEVEL HARD
a = set()
for x in range(18):
    for y in range(9, 18):
        if x < y:
            x1 = sum(c * 18 ** i for i, c in enumerate([5, x, y, 10][::-1]))
            x2 = sum(c * y ** i for i, c in enumerate([1, 8, x, 7][::-1]))
            a.add(x1+x2)
print(len(a))