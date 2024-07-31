# a = open('t.txt').readline()
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     if a[i] != a[i+1]:
#         count += 1
#         m = max(m, count)
#     else:
#         count = 1
# print(m)



# a = open('t.txt').readline()
# a = a.replace('PP', 'P P').replace('PP', 'P P')
# print(max(len(s) for s in a.split()))



# a = open('t.txt').readline()
# a = a.replace('A', 'g').replace('C', 's').replace('D', 's').replace('F', 's').replace('O', 'g')
# m = 0
# count = 0
# for i in range(0, len(a) - 1, 2):
#     if a[i] == 's' and a[i+1] == 'g':
#         count += 1
#         m = max(m, count)
#     else: count = 0
# print(m)


# a = open('t.txt').readline()
# m = 0
# count = 0
# a = a.replace('ad', 'a d').replace('da', 'd a')
# print(max(len(s) for s in a.split()))


# a = open('t.txt').readline()
# a = a.replace('NPO', '*').replace('PNO', '*')
# a = a.replace('N', ' ').replace('O', ' ').replace('P', ' ')
# print(max(len(s) for s in a.split()))



# a = open('t.txt').readline()
# m = 0
# count = 1
# a = a.replace('A', 'g').replace('B', 's').replace('C', 's').replace('D', 's').replace('O', 'g')
# for i in range(0, len(a) - 1, 2):
#     if a[i] == 's' and a[i+1] == 'g':
#         count += 1
#         m = max(count, m)
#     else:
#         count = 0
# print(m)


# a = open('t.txt').readline()
# m = 0
# count = 0
# a = a.replace('A', '0').replace('B', '0').replace('C', '0').replace('8', '1').replace('9', '1')
# for i in range(len(a) - 1):
#     if (a[i] == '0' and a[i+1] == '1') or (a[i] == '1' and a[i+1] == '0'):
#         count += 1
#         m = max(m, count)
#     else: count = 1
# print(m)



# a = open('t.txt').readline()
# for w in ('**', '++', '*+', '+*'): a = a.replace(w, ' ')
# for k in '123456789': a = a.replace(k, '1')
# m = 0
# for c in a.split():
#     if len(c) > m:
#         for i in range(len(c) - 1):
#             if c[i] not in '*+' and c[i] + c[i+1] not in ('00, 01'):
#                 sub = c[i]
#                 for j in range(i + 1, len(c)):
#                     sub += c[j]
#                 if sub[-1] not in '*+' and eval(sub) == 0:
#                     m = max(m, len(sub))
# print(m)





