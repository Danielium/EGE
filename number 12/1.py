# m = float('inf')
# for n in range(4, 2000):
#     s = '3' * n + '5'
#     while '23' in s or '5333' in s or '33333' in s:
#         if '23' in s:
#             s = s.replace('23', '3', 1)
#         if '5333' in s:
#             s = s.replace('5333', '32', 1)
#         if '33333' in s:
#             s = s.replace('33333', '55', 1)
#     m = min(m, sum(map(int, s)))
# print(m)


# for n in range(4, 10000):
#     s = '5' + n * '2'
#     while '52' in s or '2222' in s or '1122' in s:
#         if '52' in s: s = s.replace('52', '11')
#         if '2222' in s: s = s.replace('2222', '5')
#         if '1122' in s: s = s.replace('1122', '25')
#     if sum(map(int, s)) == 64:
#         print(n)

# m = -float('inf')
# for n in range (4, 1000):
#     s = '1' + '2' * n
#     while '12' in s or '322' in s or '222' in s:
#         if '12' in s: s = s.replace('12', '2', 1)
#         if '322' in s: s = s.replace('322', '21', 1)
#         if '222' in s: s = s.replace('222', '3', 1)
#     m = max(m, len(s))
# print(m)

# m = -float('inf')
# for n in range(4, 10000):
#     s =  '1' + '2' * n
#     while '12' in s or '322' in s or '222' in s:
#         if '12' in s: s = s.replace('12', '2', 1)
#         if '322' in s: s = s.replace('322', '21', 1)
#         if '222' in s: s = s.replace('222', '3', 1)
#     m = max(m, sum(map(int, s)))
# print(m)


# for n in range(101, 1000):
#     s = '5' * n
#     while '555' in s or '11' in s or '2' in s:
#         if '555' in s: s = s.replace('555', '1', 1)
#         if '11' in s: s = s.replace('11', '25', 1)
#         if '2' in s: s = s.replace('2', '5', 1)
#         if s == '15': print(n)


# for n in range(4, 1000):
#     s = '2' + '5' * n
#     while '25' in s or '35' in s or '555' in s:
#         if '25' in s: s = s.replace('25', '53', 1)
#         if '35' in s: s = s.replace('35', '2', 1)
#         if '555' in s: s = s.replace('555', '23', 1)
#     if sum(map(int, s)) % 7 == 0: print(n)

# count  = 0
# for n in range(1000, 2001):
#     s = '7' + '8' * n
#     while '78' in s or '888' in s:
#         if '78' in s: s = s.replace('78', '8')
#         if '888' in s: s = s.replace('888', '7')
#         if sum(map(int, s)) == 16: count += 1
# print(count)


# for n in range(1, 1000):
#     s = '4' + '6' * n
#     while '46' in s or '666' in s:
#         if '46' in s: s = s.replace('46', '5', 1)
#         if '666' in s: s = s.replace('666', '4', 1)
#     if sum(map(int, s)) > 1000: print(n)


#  for n in range(6, 1000):
#      s = '1' + '3' * n
#      while '12' in s or '233' in s or '3333' in s:
#          if '12' in s: s = s.replace('12', '322', 1)
#          if '233' in s: s = s.replace('233', '23', 1)
#          if '3333' in s: s = s.replace('3333', '32', 1)
#      if sum(map(int, s)) % 6 == 0: print(n)


# for n in range(11, 1000):
#     s = '3' + '5' * n
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s: s = s.replace('25', '32', 1)
#         if '355' in s: s = s.replace('355', '25', 1)
#         if '555' in s: s = s.replace('555', '3', 1)
#     if sum(map(int, s)) % 25 == 0: print(n, sum(map(int, s)))













# s = 65 * '8'
# while '222' in s or '888' in s:
#     if '222' in s:
#         s = s.replace('222', '8')
#     else:
#         s = s.replace('888', '2')
# print(s)



# s = 65 * '5'
# while '333' in s or '555' in s:
#     if '555' in s:
#         s = s.replace('555', '3')
#     else:
#         s = s.replace('333', '5')
# print(s)



s = 72 * '5'
while '333' in s or '555' in s:
    if '555' in s:
        s = s.replace('555', '3')
    else:
        s = s.replace('333', '5')
print(s)






















