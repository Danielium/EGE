# from ipaddress import *
# for a in range(256):
#     net = ip_network(f'183.192.{a}.0/255.255.252.0', 0)
#     if all(f'{ip:b}'[16:].count('1') > 3 for ip in net):
#         print(a)
#         break
# 60 № 12467


# from ipaddress import *
# counter = 0
# for a in range(256):
#     net = ip_network(f'207.0.{a}.167/255.255.255.192', 0)
#     if all(f'{ip:b}'[:16].count('0') > f'{ip:b}'[16:].count('0') for ip in net):
#         counter += 1
# print(counter)
#  37 № 11835


# from ipaddress import *
# for a in range(256):
#     net = ip_network(f'248.112.{a}.35/255.255.255.240', 0)
#     if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0') for ip in net):
#         print(a)
# 224 № 11784




