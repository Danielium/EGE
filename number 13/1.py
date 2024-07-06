# from ipaddress import *
# net = ip_network('136.36.240.16/255.255.255.248',0)
# counter = 0
# for ip in net:
#     if f'{ip:b}'.count('101') == 0:
#         counter += 1
# print(counter)
#4   № 12922


# from ipaddress import *
# net = ip_network('192.168.32.48/255.255.255.240', 0)
# counter = 0
# for ip in net:
#     if f'{ip:b}'.count('1') % 2 != 0:
#         counter += 1
# print(counter)
# 8 № 12245


# from ipaddress import *
# net = ip_network('129.128.0.0/255.128.0.0', 0)
# print(min(f'{ip:b}'.count('0') for ip in net))
# 6 № 11782


# from ipaddress import *
# count = 0
# net = ip_network('192.168.32.160/255.255.255.240', 0)
# for ip in net:
#     if f'{ip:b}'.count('1') % 2 == 0:
#         count += 1
# print(count)


# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'215.181.200.27/{m}', 0)
#     if str(net.network_address) == '215.181.192.0':
#         print(net.netmask)


# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'148.195.140.28/{m}', 0)
#     if str(net.network_address) == '148.195.140.0':
#         print(m)


# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'241.185.253.57/{m}', 0)
#     if str(net.network_address) == '241.185.252.0':
#         print(32 - m)


# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'208.207.230.65/{m}', 0)
#     if str(net.network_address) == '208.207.224.0':
#         print('Йоу')



# from ipaddress import *
# net = ip_network('156.132.15.138/255.255.252.0', 0)
# for n, ip in enumerate(net.hosts()):
#     print(n + 1, ip)



# from ipaddress import *
# for m in range(33):
#     net1 = ip_network(f'157.127.182.76/{m}', 0)
#     net2 = ip_network(f'157.127.190.80/{m}', 0)
#     if net1.network_address != net2.network_address:
#         print(m)


# from ipaddress import *
# count = 0
# net = ip_network('192.168.240.0/255.255.255.0', 0)
# for ip in net:
#     if f'{ip:b}'.count('1') == f'{ip:b}'.count('0'):
#         count += 1
# print(count)



# from ipaddress import *
# count = 0
# net = ip_network('112.154.133.208/255.255.252.0', 0)
# for ip in net:
#     if f'{ip:b}'[:16].count('1') <= f'{ip:b}'[16:].count('0') and f'{ip:b}'[16:].count('0') % 2 != 0:
#         count += 1
# print(count)



# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'145.192.94.230/{m}', 0)
#     if str(net.network_address) == '145.192.80.0':
#         print(net.netmask)


from ipaddress import *
count = 0
net = ip_network('192.168.240.0/255.255.255.0', 0)
for ip in net:
    if f'{ip:b}'.count('1') == f'{ip:b}'.count('0'):
        count += 1
print(count)