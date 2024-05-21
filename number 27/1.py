# f = open('file.t.txt')
# K = int(f.readline())
# N = int(f.readline())
# a = [int(f.readline()) for i in range(N)]
# m = -float('inf')
# for i in range(N - 2):
#     for j in range((N-1)):
#         if j - i >= K:
#             m = max(m, sum(a[i:j+1]))
# print(m)

# f = open('file.t.txt')
# K = int(f.readline())
# N = int(f.readline())
# a = [int(f.readline()) for i in range(N)]
# m = -float('inf')
# for i in range(N-2):
#     for j in range(i +1, N-1):
#         for k in range(j + 1, N):
#             if j - i >= K and k - i >= K and k - j >= K:
#                 m = max(m, a[i]+a[j]+a[k])
# print(m)


# f = open('file.t.txt')
# K = int(f.readline())
# N = int(f.readline())
# a = [int(f.readline()) for i in range(N)]
# m = 0
# for i in range(N-1):
#     for j in range(i+1, N):
#         if a[i] + a[j] >= K:
#             m += 1
# print(m)



# f = open('file.t.txt')
# K = int(f.readline())
# N = int(f.readline())
# a = [int(f.readline()) for i in range(N)]
# m = -float('inf')
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             if j - i >= K and k - i >= K and k - j >= K:
#                 if (a[i] * a[j] * a[k]) % 2023 == 0:
#                     m = max(m, a[i] * a[j] * a[k])
# print(m)



# f = open('file.t.txt')
# K = int(f.readline())
# N = int(f.readline())
# a = [int(f.readline()) for i in range(N)]
# m = -float('inf')
# for i in range(N-1):
#     for j in range(i+1, N):
#         if j - i >= K:
#             m = max(m, a[i] + a[j])
# print(m)


f = open('file.txt')
K = 113
N = int(f.readline())
a = [int(f.readline()) for i in range(N)]
m = -float('inf')
m_l = -float('inf')
for i in range(N-1):
    for j in range(i+1, N):
        if sum(a[i:j+1]) % K == 0 and sum(a[i:j+1]) >= m:
            m = sum(a[i:j+1])
            m_l = max(m_l, len(a[i:j+1]))
print(m_l)