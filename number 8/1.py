# from itertools import product
# s = list(product('БМНРЮ', repeat=6))
# counter = 0
# for x in s:
#     counter += 1
#     if x[0] != 'М' and x.count('Р') >= 2 and x.count('Ю') == 0 and counter % 2 != 0:
#         print(counter)
# 11719

# from itertools import product
# s = list(product('АЖЗОПЮ', repeat=6))
# counter = 0
# n = 0
# for x in s:
#     counter += 1
#     if x[0] == 'А' and x.count('З') >= 2 and counter % 2 == 0:
#         n+=1
# print(n)
# 513


# from itertools import product
# s = list(product('ИРЩЮ', repeat=5))
# counter = 0
# for x in s:
#     counter += 1
#     if x[0] == 'Щ' and x[-1] == 'И':
#         print(counter)
# 765

# from itertools import product
# counter = 0
# s = list(product('ДРСЩЭ', repeat=4))
# for x in s:
#     x = ''.join(x)
#     counter += 1
#     if x == 'ЩДЩД':
#         print(counter)
# 391


# from itertools import product
# count = 0
# s = list(product('ГИНРЧ', repeat=5))
# for x in s:
#     x = ''.join(x)
#     count += 1
#     if count == 415:
#         print(x)
#         break
# ГРИНЧ


# from itertools import product
# count = 0
# l = list(product('ГЕПАРД', repeat = 5))
# for s in l:
#     if s.count('Г') == 1 and s[0] != 'А' and s[-1] != 'Е':
#         count += 1
# print(count)
# №1852


# from itertools import permutations, product
# l = list(set(permutations('АНАСТАСИЯ', r = 9)))
# notl1 = list(product('АИЯ', repeat = 3))
# notl2 = list(product('НСТ', repeat = 3))
# count = 0
# for s in l:
#     if not (any(''.join(n) in ''.join(s) for n in notl1) and any(''.join(n) in ''.join(s) for n in notl2)):
#         count += 1
#
# print(count)

# from itertools import product
# l = list(product('ЕЛМРУ', repeat = 4))
# count = 0
# for i in l:
#     count += 1
#     print(count, *i)

# from itertools import product
# l = list(product('АГМНСТУ', repeat = 6))
# count = 0
# for i in l:
#     count += 1
#     if i[0] != 'У' and i.count('М') == 2 and i.count('Г') <= 1:
#         print(count, *i)

# from itertools import product
# count = 0
# l = list(product('ЕКМОПРТЬЮ', repeat = 5))
# for i in l:
#     count += 1
#     if i[0] != 'Ь' and i.count('К') == 2:
#         if count % 2 != 0:
#             print(count, i)

# from itertools import product
# count1 = 0
# count2 = 0
# l = list(product('ЬРПЛЕА', repeat = 5))
# for i in l:
#     count1 += 1
#     if i[-1] == 'Ь':
#         count2 += 1
#     if count1 == 387:
#         break
# print(count2)

# from itertools import product
# count = 0
# l = list(product('АЕЛМНОРЬ', repeat = 6))
# for i in l:
#     i = ''.join(i)
#     count += 1
#     if i == 'НЕНОРМ':
#         print(count)
# print(154817 -137588 - 1)


# from itertools import product
# count = 0
# l = list(product('АГДИЛНРЯ', repeat = 6))
# for i in l:
#     i = ''.join(i)
#     count += 1
#     if i[0] != 'Я' and i.count('Д') == 3 and count % 2 == 0:
#         print(count)

# from itertools import product
# count = 0
# l = list(product('БГДНОУШ', repeat = 6))
# for i in l:
#     i = ''.join(i)
#     count += 1
#     if i[0] != 'Б' and i.count('Н') >= 2 and count % 2 != 0:
#         print(count)

# from itertools import product
# count = 0
# l = list(product('БМНРЮ', repeat = 6))
# for i in l:
#     i = ''.join(i)
#     count += 1
#     if i[0] != 'М' and i.count('Р') >= 2  and i.count('Ю') == 0 and count % 2 != 0:
#         print(count)

#from itertools import product
#count = 0
#c = 0
#l = list(product('АГИЛМОРФ', repeat = 5))
#for i in l:
#    i = ''.join(i)
#    count += 1
#    if i[:2] != 'ЛМ' and i.count('И') >= 2 and count % 2 == 0:
#        c += 1
#        print(c)

# from itertools import product
# count = 0
# l = list(product('АКЛМНЯ', repeat = 5))
# for i in l:
#     i = ''.join(i)
#     count += 1
#     if i[:2] == 'МН':
#         print(count)
# print(4966 - 4753)

from itertools import product
count = 0
l = list(product('ABCX', repeat = 5))
for i in l:
    if (i[-1] == 'X' and i.count('X') == 1) or i.count('X') == 0:
        count += 1
print(count)