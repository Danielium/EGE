# clustersA = [[], []]
# clustersB = [[], [], []]
# for line in open('27A.txt'):
#     x, y = [float(k) for k in line.split()]
#     if y<3:
#         clustersA[0].append([x, y])
#     else:
#         clustersA[1].append([x, y])
# for line in open('27B.txt'):
#     x, y = [float(k) for k in line.split()]
#     if y < 3: clustersB[0].append([x, y])
#     elif y < 7: clustersB[1].append([x, y])
#     else: clustersB[2].append([x, y])
# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2-x1)**2 + (y2-y1)**2)**0.5
# def center(cl):
#     m = []
#     for p in cl:
#         sm = sum(d(p, p1) for p1 in cl)
#         m.append([sm, p])
#     return min(m)[1]
#
# centersA = [center(cl) for cl in clustersA]
# centersB = [center(cl) for cl in clustersB]
# pxA = sum(x for x, y in centersA)/2 * 10000
# pyA = sum(y for x, y in centersA)/2 * 10000
# pxB = sum(x for x, y in centersB)/3 * 10000
# pyB = sum(y for x, y in centersB)/3 * 10000
# print(int(pxA), int(pyA))
# print(int(pxB), int(pyB))


# clustersA = [[],[]]
# clustersB = [[],[],[]]
# for line in open('27A_18623.txt'):
#     x, y = [float(k) for k in line.split()]
#     if y < 3: clustersA[0].append([x, y])
#     else: clustersA[1].append([x, y])
# for line in open('27B_18623'):
#     x, y = [float(k) for k in line.split()]
#     if y < -x+8: clustersB[0].append([x, y])
#     elif y < 1.5*x-6.5: clustersB[1].append([x, y])
#     else: clustersB[2].append([x, y])
# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2-x1)**2 + (y2-y1)**2)**0.5
# def center(cl):
#     m = []
#     for p in cl:
#         sm = sum(d(p, p1) for p1 in cl)
#         m.append([sm, p])
#     return min(m)[1]
#
# centersA = [center(cl) for cl in clustersA]
# centersB = [center(cl) for cl in clustersB]
# pxA = sum(x for x, y in centersA)/2 * 100000
# pyA = sum(y for x, y in centersA)/2 * 100000
# pxB = sum(x for x, y in centersB)/3 * 100000
# pyB = sum(y for x, y in centersB)/3 * 100000
# print(int(pxA), int(pyA))
# print(int(pxB), int(pyB))


# a --- y = 3
# b --- y=3 y=7

# clustersA = [[], []]
# clustersB = [[],[],[]]
# for line in open('27A_17882'):
#     x, y = [float(k) for k in line.split()]
#     if y <= 3: clustersA[0].append([x, y])
#     else: clustersA[1].append([x, y])
# for line in open('27B_17882'):
#     x, y = [float(k) for k in line.split()]
#     if y <= 3: clustersB[0].append([x, y])
#     if y <= 7: clustersB[1].append([x, y])
#     else: clustersB[2].append([x, y])
# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2-x1)**2 + (y2-y1)**2)**0.5
# def center(cl):
#     m = []
#     for p in cl:
#         sm = sum(d(p, p1) for p1 in cl)
#         m.append([sm, p])
#     return min(m)[1]
# centersA = [center(cl) for cl in clustersA]
# centersB = [center(cl) for cl in clustersB]
# pxA = sum(x for x, y in centersA)/2 * 10000
# pyA = sum(y for x, y in centersA)/2 * 10000
# pxB = sum(x for x, y in centersB)/3 * 10000
# pyB = sum(y for x, y in centersB)/3 * 10000
# print(int(pxA), int(pyA))
# print(int(pxB), int(pyB))



cluster_A = [[], []]
cluster_B = [[], [], [], [], []]
for line in open('27_A_17916.txt'):
    x, y = [float(x) for x in line.split()]
    if y > 8:
        cluster_A[1].append([x, y])
    else:
        cluster_A[0].append([x, y])
for line in open('27_B_17916.txt'):
    x, y = [float(x) for x in line.split()]
    if x > 12:
        cluster_B[0].append([x, y])
    elif y < 5:
        cluster_B[1].append([x, y])
    elif y < 9:
        cluster_B[2].append([x, y])
    elif y < 13:
        cluster_B[3].append([x, y])
    else:
        cluster_B[4].append([x, y])
def d(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
def centres(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]
centersA = [centres(cl) for cl in cluster_A]
centersB = [centres(cl) for cl in cluster_B]

pxA = sum(x for x, y in centersA) / 2 * 10000
pyA = sum(y for x, y in centersA) / 2 * 10000
pxB = sum(x for x, y in centersB) / 5 * 10000
pyB = sum(y for x, y in centersB) / 5 * 10000
print(pxA, pyA)
print(pxB, pyB)