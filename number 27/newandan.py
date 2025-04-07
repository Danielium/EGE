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







#1

# data = []
# for line in open('27B.txt'):
#     a = [float(x) for x in line.split()]
#     data.append(a)
# print(len(data))
#
# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2-x1)**2 + (y2-y1)**2)**0.5
#
# def get_cluster(p0):
#     cluster = [p for p in data if d(p0, p) < 1] # создаем список таких точек-соседей, для которых расстояние от p0 до них самих меньше какого-то значения. Сюда же и войдет сама p0, тк от p0 до p0 расстояние 0
#     if len(cluster) > 0: #если такие соседи есть, то
#         for p in cluster: data.remove(p) #удаляем эту точку и ее соседей из даты, чтобы их больше не чекать
#         next_clusters = [get_cluster(p) for p in cluster] #для каждого соседа и самой точки(что бессмысленно, так как мы ее соседей удалили из даты) ищем еще соседей
#         cluster += sum(next_clusters, []) #эти соседние точки добавляем в cluster. Тк они в одном кластере
#     return cluster
#
# clusters = []
#
# while len(data) > 0: #пока у нас не закончились точки в дате
#     cluster = get_cluster(data[0]) #берем каждую точку и производим с ней те действия, которые описаны выше
#     print(len(cluster))
#     clusters.append(cluster)  #добавляем этот отдельный кластер в список кластеров
#
# def center(cl):
#     m = []
#     for p in cl:
#         sm = sum(d(p1, p) for p1 in cl)
#         m.append([sm, p])
#     return min(m)[1]
#
#
# centers = [center(cl) for cl in clusters]
# px = sum(x for x, y in centers) / len(centers) * 10000
# py = sum(y for x, y in centers) / len(centers) * 10000
# print(int(px), int(py))
#A 10738 30730
#B 37522 51277


#2

# data = []
# for line in open('27B2.txt'):
#     line = line.replace(',','.')
#     a = [float(x) for x in line.split()]
#     data.append(a)
#
# print(len(data))
#
# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2-x1)**2 + (y2-y1)**2)**0.5
#
# def get_cluster(p0):
#     cluster = [p for p in data if d(p0, p) < 1]
#     if len(cluster) > 0:
#         for p in cluster: data.remove(p)
#         next_cluster = [get_cluster(p) for p in cluster]
#         cluster += sum(next_cluster, [])
#     return cluster
#
# clusters = []
#
# while len(data) != 0:
#     cluster = get_cluster(data[0])
#     print(len(cluster))
#     clusters.append(cluster)
#
# def center(cluster):
#     m = []
#     for p in cluster:
#         sm = sum(d(p, p1) for p1 in cluster)
#         m.append([sm, p])
#     return min(m)[1]
#
# centers = [center(cl) for cl in clusters]
#
# px = sum(x for x, y in centers) / len(centers) * 10000
# py = sum(y for x, y in centers) / len(centers) * 10000
#
# print(int(px), int(py))

#A 95200 233468
#B 163215 128141


#3

# data = []
#
# for line in open('27A3.txt'):
#     line = line.replace(',','.')
#     a = [float(x) for x in line.split()]
#     data.append(a)
#
# print(len(data))
#
# def d(A, B):
#     x1,y1 = A
#     x2, y2 = B
#     return ((x2-x1)**2 + (y2-y1)**2)**0.5
#
# def get_cluster(p0):
#     cluster = [p for p in data if d(p0, p) < 1]
#     if len(cluster) > 0:
#         for p in cluster: data.remove(p)
#         next_cluster = [get_cluster(p) for p in cluster]
#         cluster += sum(next_cluster, [])
#     return cluster
#
# clusters = []
#
# while len(data) != 0:
#     cluster = get_cluster(data[0])
#     print(len(cluster))
#     clusters.append(cluster)
#
# def center(cluster):
#     m = []
#     for p in cluster:
#         sm = sum(d(p, p1) for p1 in cluster)
#         m.append([sm, p])
#     return min(m)[1]
#
# centers = [center(cl) for cl in clusters]
#
# px = (sum(x for x, y in centers) / len(centers)) * 100000
# py = (sum(y for x, y in centers) / len(centers)) * 100000
#
# print(int(px), int(py))

#A 398800 348577
#B 596884 400991



# 4

# data = []
# for line in open('27B4.txt'):
#     line = line.replace(',', '.')
#     a = [float(x) for x in line.split()]
#     data.append(a)
#
# print(len(data))
#
# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2-x1)**2 + (y2-y1)**2)**0.5
#
# def get_cluster(p0):
#     cluster = [p for p in data if d(p0, p) < 1.1]
#     if len(cluster) > 0:
#         for p in cluster: data.remove(p)
#         next_clusters = [get_cluster(p) for p in cluster]
#         cluster += sum(next_clusters, [])
#     return cluster
#
# clusters = []
#
# while len(data) != 0:
#     cluster = get_cluster(data[0])
#     print(len(cluster))
#     clusters.append(cluster)
#
# def center(cl):
#     m = []
#     for p in cl:
#         sm = sum(d(p, p1) for p1 in cl)
#         m.append([sm, p])
#     return min(m)[1]
#
# centres = [center(cl) for cl in clusters]
#
# px = ((sum(x for x, y in centres)) / len(centres)) * 100000
# py = ((sum(y for x, y in centres)) / len(centres)) * 100000
#
# print(int(px), int(py))

#A 435739 471100
#B 250615 150222




data = []

for line in open('27B5.txt'):
    line = line.replace(',', '.')
    a = [float(x) for x in line.split()]
    data.append(a)

print(len(data))

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

def get_cluster(p0):
    cluster = [p for p in data if d(p0, p) < 1]
    if len(cluster) > 0:
        for p in cluster: data.remove(p)
        next_cluster = [get_cluster(p) for p in cluster]
        cluster += sum(next_cluster, [])
    return cluster

clustres = []

while len(data) != 0:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clustres.append(cluster)

def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


centres = [center(cl) for cl in clustres]

px = (sum(x for x, y in centres) / len(centres)) * 100000
py = (sum(y for x, y in centres) / len(centres)) * 100000

print(int(px), int(py))

#A 752263 548854
#B 767186 281688





























