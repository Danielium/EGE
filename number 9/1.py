# count = 0
# for line in open('t.t.txt'):
#     a = [int(x) for x in line.split()]
#     p4 = [x for x in a if a.count(x) == 4]
#     p2 = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     if len(np) == 3 and len(p2) == 2 and len(p4) == 4:
#         if sum(np) / len(np) >= max(p4 + p2):
#             count += 1
# print(count)



# for line in open('t.t.txt'):
#     a = [int(x) for x in line.split()]
#     p2 = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p2) == 4 and len(np) == 2 and a.count(max(a)) == 1:
#         if max(a) * min(a) > sum(a) - max(a) - min(a):
#             print(sum(a))
#             break

# count = 0
# for line in open('t.t.txt'):
#     a = [int(x) for x in line.split()]
#     p2 = [x for x in a if a.count(x) == 2]
#     np = sum(a) - sum(p2)
#     if len(p2) == 6:
#         if (min(a) + max(a)) / 2 < np:
#             count += 1
# print(count)



# count = 0
# for line in open('t.t.txt'):
#     a = [int(x) for x in line.split()]
#     p2 = [x for x in a if a.count(x) == 2]
#     np = [x for x in a if a.count(x) == 1]
#
#     if len(p2) == 4 and len(np) == 3:
#         if (p2[0] * p2[1] * p2[2] * p2[3]) / (np[0] * np[1] * np[2]) > 2:
#             count += 1
# print(count)



# count = 0
# for line in open('t.t.txt'):
#     a = [int(x) for x in line.split()]
#     p3 = [x for x in a if a.count(x) == 3]
#     np = [x for x in a if a.count(x) == 1]
#     u1 = len(p3) == 3 and len(np) == 4
#     u2 = a == sorted(a)
#
#     if u1 + u2 <= 1:
#         count += 1
# print(count)




# count = 0
# for line in open('t.t.txt'):
#     a = [int(x) for x in line.split()]
#     p3 = [x for x in a if a.count(x) == 3]
#     np = [x for x in a if a.count(x) == 1]
#     count += 1
#     if len(p3) == 3 and len(np) == 4:
#         if sum(p3)/len(p3) > sum(np)/len(np):
#             print(count)




# count = 0
# for line in open('t.t.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) > 1]
#     if a.count(min(a)) == 1:
#         if max(a) + min(a) < sum(p):
#             count += 1
# print(count)




# count = 0
# for line in open('t.t.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) > 1]
#     u1 = len(p) > 0
#     a.sort()
#     u2 = a[1] - a[0] == a[2] - a[1] == a[3] - a[2] == a[4] - a[3] == a[5] - a[4]
#     if u1 + u2 >= 1:
#         count += 1
# print(count)



# count = 0
# for line in open('t.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) == 1]
#     ch = [x for x in a if x % 2 == 0]
#     nch = [x for x in a if x % 2 == 1]
#     if len(p) == 6:
#         if len(ch) > len(nch):
#             count += 1
#
# print(count)


# count = 0
# for line in open('t.txt'):
#     a = [int(x) for x in line.split()]
#     p = [x for x in a if a.count(x) > 1]
#     if a.count(min(a)) == 1:
#         if max(a) + min(a) < sum(p):
#             count += 1
# print(count)

# count = 0
# for line in open('t.txt'):
#     a = [int(x) for x in line.split()]
#     p = []
#     np = []
#     for x in a:
#         if a.count(x) == 2: p.append(x)
#         if a.count(x) == 1: np.append(x)
#     if len(p) == 4:
#         p = list(set(p))
#         print(p, np)
#         if (np[0] > p[0] and np[0] < p[1]) or (np[0] < p[0] and np[0] > p[1]):
#             count += 1
# print(count)


# count = 0
# for line in open('t.txt'):
#     a = [int(x) for x in line.split()]
#     np = [x for x in a if a.count(x) == 1]
#     p = [x for x in a if a.count(x) == 3]
#     if len(set(p)) == 1 and len(set(np)) == 3:
#         if sum(p) ** 2 > sum(np) ** 2:
#             count += 1
# print(count)


# count = 0
# for line in open('t.txt'):
#     a = sorted([int(x) for x in line.split()])
#     p = [x for x in a if a.count(x) == 2]
#     if a[3] < a[0]+a[1]+a[2] and len(p) == 2:
#         count += 1
# print(count)



# count = 0
# for line in open('t.txt'):
#     a = sorted([int(x) for x in line.split()])
#     if (a[0] + a[2])/2 <= a[1]:
#         count += 1
# print(count)

# count = 0
# for line in open('t.txt'):
#     a = sorted([int(x) for x in line.split()])
#     if a[0] + a[3] < a[2] + a[1]:
#         count += 1
# print(count)

# count = 0
# for line in open('t.txt'):
#     a = sorted([int(x) for x in line.split()])
#     if a[2] ** 2 > a[1] * a[0] * 2:
#         count += 1
# print(count)

# count = 0
# for line in open('t.txt'):
#     a = sorted([int(x) for x in line.split()])
#     p3 = [x for x in a if a.count(x) == 3]
#     np = [x for x in a if a.count(x) == 1]
#     if (len(p3) == 3 and len(np) == 3) + ((a[0] + a[5]) ** 2 > a[1] ** 2 + a[2] ** 2 + a[3] ** 2 + a[4] ** 2) >= 1:
#         count += 1
# print(count)



# count = 0
# for line in open('t.txt'):
#     a = [int(x) for x in line.split()]
#     p3 = [x for x in a if a.count(x) == 3]
#     np = [x for x in a if a.count(x) == 1]
#     if len(p3) == 3 and len(np) == 4:
#         if (sum(np) / 4) <= p3[0]: count += 1
#
# print(count)

# count = 0
# for line in open('t.txt'):
#     c = [int(x) for x in line.split()]
#     p = [x for x in c if c.count(x)==2]
#     if len(p) == 2:
#         if max(c) < sum(c) - max(c):
#             count += 1
# print(count)



# count = 0
# for line in open('t.txt'):
#     c = [int(x) for x in line.split()]
#     p = [x for x in c if c.count(x)==3]
#     np = [x for x in c if c.count(x)==1]
#     if len(p) == 3:
#         if len(np) == 3:
#             if sum(np)/3 <= sum(p):
#                 count += 1
# print(count)



# count = 0
# for line in open('t.txt'):
#     c = [int(x) for x in line.split()]
#     p = [x for x in c if c.count(x) == 3]
#     np = [x for x in c if c.count(x) == 1]
#     if len(p) == 3:
#         if len(np) == 3:
#             if sum(p)**2 > sum(np)**2:
#                 count += 1
# print(count)



# count = 0
# for line in open('t.txt'):
#     c = [int(x) for x in line.split()]
#     p = [x for x in c if c.count(x)==2]
#     if len(p) == 2:
#         if max(c) < sum(c) - max(c):
#             count += 1
# print(count)


# count = 0
# for line in open('t.txt'):
#     c = [int(x) for x in line.split()]
#     p = [x for x in c if c.count(x) == 3]
#     np = [x for x in c if c.count(x) == 1]
#     if len(p) == 3 and len(np) == 3:
#         if sum(p)**2 > sum(np)**2:
#             count += 1
# print(count)

count = 0
for line in open('t.txt'):
    c = [int(x) for x in line.split()]
    np = [x for x in c if c.count(x)==1]
    tr = [x for x in c if c.count(x)==3]
    if len(tr)==3:
        if len(np) == 3:
            if (sum(np))**2 < (sum(tr))**2:
                count += 1
print(count)








